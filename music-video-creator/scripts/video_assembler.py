import os
import argparse
import subprocess
import glob
import random

def get_audio_duration(audio_file):
    """Get audio duration in seconds using ffprobe."""
    cmd_duration = [
        "ffprobe", 
        "-v", "error", 
        "-show_entries", "format=duration", 
        "-of", "default=noprint_wrappers=1:nokey=1", 
        audio_file
    ]
    try:
        duration_str = subprocess.check_output(cmd_duration).decode().strip()
        return float(duration_str)
    except Exception as e:
        print(f"Error getting audio duration: {e}")
        return None

def generate_srt_file(lyrics_file, audio_duration, output_srt):
    """Generate an SRT subtitle file from lyrics."""
    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    if not lines:
        print("No lyrics found in file.")
        return None
    
    duration_per_line = audio_duration / len(lines)
    
    with open(output_srt, 'w', encoding='utf-8') as f:
        for i, line in enumerate(lines):
            start_time = i * duration_per_line
            end_time = (i + 1) * duration_per_line
            start_formatted = format_srt_time(start_time)
            end_formatted = format_srt_time(end_time)
            f.write(f"{i + 1}\n")
            f.write(f"{start_formatted} --> {end_formatted}\n")
            f.write(f"{line}\n\n")
    
    print(f"Generated subtitles: {output_srt} ({len(lines)} lines)")
    return output_srt

def format_srt_time(seconds):
    """Format seconds as SRT timestamp (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def get_ken_burns_filter(index, duration, direction="random"):
    """
    Generate Ken Burns effect filter for an image.
    Creates zoom in/out with pan effect.
    """
    # Define different Ken Burns movements
    movements = [
        # Zoom in from center
        f"scale=8000:-1,zoompan=z='min(zoom+0.0015,1.5)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(duration*30)}:s=1920x1080:fps=30",
        # Zoom out from center  
        f"scale=8000:-1,zoompan=z='if(lte(zoom,1.0),1.5,max(1.001,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(duration*30)}:s=1920x1080:fps=30",
        # Pan left to right with slight zoom
        f"scale=8000:-1,zoompan=z='min(zoom+0.001,1.3)':x='if(lte(on,1),0,min(x+2,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d={int(duration*30)}:s=1920x1080:fps=30",
        # Pan right to left with slight zoom
        f"scale=8000:-1,zoompan=z='min(zoom+0.001,1.3)':x='if(lte(on,1),iw,max(x-2,0))':y='ih/2-(ih/zoom/2)':d={int(duration*30)}:s=1920x1080:fps=30",
        # Zoom in from top-left
        f"scale=8000:-1,zoompan=z='min(zoom+0.0015,1.5)':x='iw/4-(iw/zoom/4)':y='ih/4-(ih/zoom/4)':d={int(duration*30)}:s=1920x1080:fps=30",
        # Zoom in from bottom-right
        f"scale=8000:-1,zoompan=z='min(zoom+0.0015,1.5)':x='iw*3/4-(iw/zoom/2)':y='ih*3/4-(ih/zoom/2)':d={int(duration*30)}:s=1920x1080:fps=30",
    ]
    
    if direction == "random":
        return movements[index % len(movements)]
    elif direction == "zoom_in":
        return movements[0]
    elif direction == "zoom_out":
        return movements[1]
    else:
        return movements[index % len(movements)]

def create_title_clip(title, output_path, duration=3, is_outro=False):
    """Create an intro or outro title clip with the song name."""
    
    # Remove special characters that cause FFmpeg issues
    safe_title = title.replace("'", "").replace('"', "").replace(":", " -").replace("\\", "")
    # Keep accented characters but escape for FFmpeg
    
    if is_outro:
        # Outro with "Gracias por escuchar"
        text_filter = (
            f"drawtext=text='{safe_title}':fontsize=72:fontcolor=white:"
            f"x=(w-text_w)/2:y=(h-text_h)/2-50:shadowcolor=black:shadowx=3:shadowy=3,"
            f"drawtext=text='Gracias por escuchar':fontsize=36:fontcolor=white:"
            f"x=(w-text_w)/2:y=(h-text_h)/2+50:shadowcolor=black:shadowx=2:shadowy=2"
        )
    else:
        # Intro with just the title
        text_filter = (
            f"drawtext=text='{safe_title}':fontsize=80:fontcolor=white:"
            f"x=(w-text_w)/2:y=(h-text_h)/2:shadowcolor=black:shadowx=3:shadowy=3"
        )
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"color=c=black:s=1920x1080:d={duration}",
        "-vf", text_filter,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        output_path
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"Created {'outro' if is_outro else 'intro'}: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating title clip: {e.stderr if e.stderr else e}")
        return False

def get_song_name_from_file(audio_file):
    """Extract song name from audio filename."""
    basename = os.path.basename(audio_file)
    name = os.path.splitext(basename)[0]
    return name

def add_watermark_filter(base_filter="", watermark_text="Suscríbete"):
    """Add a watermark text to bottom-right corner."""
    watermark = (
        f"drawtext=text='{watermark_text}':fontsize=28:fontcolor=white@0.8:"
        f"x=w-text_w-30:y=h-text_h-30:font=Arial:shadowcolor=black@0.6:shadowx=2:shadowy=2"
    )
    if base_filter:
        return f"{base_filter},{watermark}"
    return watermark

def assemble_video_advanced(images_dir, audio_file, output_file, image_duration=None, 
                           lyrics_file=None, font_size=48, transitions=False, 
                           ken_burns=False, transition_duration=1.0):
    """
    Assembles a video with advanced effects.
    
    Args:
        images_dir: Directory containing images
        audio_file: Path to audio file
        output_file: Output video filename
        image_duration: Seconds per image (None = auto-calculate)
        lyrics_file: Optional path to lyrics for subtitles
        font_size: Subtitle font size
        transitions: Enable crossfade transitions
        ken_burns: Enable Ken Burns zoom/pan effect
        transition_duration: Duration of crossfade in seconds
    """
    # Validate inputs
    if not os.path.exists(images_dir):
        print(f"Error: Image directory '{images_dir}' not found.")
        return False
    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found.")
        return False

    # Find images
    images = sorted(glob.glob(os.path.join(images_dir, "*.jpg")))
    if not images:
        images = sorted(glob.glob(os.path.join(images_dir, "*.png")))
    if not images:
        print(f"Error: No images found in '{images_dir}'.")
        return False

    print(f"Found {len(images)} images.")
    
    # Get audio duration
    audio_duration = get_audio_duration(audio_file)
    if audio_duration is None:
        return False
    print(f"Audio duration: {audio_duration:.2f} seconds")

    # Calculate duration per image
    if image_duration:
        calc_duration = float(image_duration)
    else:
        calc_duration = audio_duration / len(images)
    print(f"Duration per image: {calc_duration:.2f} seconds")

    # Generate subtitles if lyrics provided
    srt_file = None
    if lyrics_file and os.path.exists(lyrics_file):
        srt_file = os.path.join(images_dir, "subtitles.srt")
        generate_srt_file(lyrics_file, audio_duration, srt_file)

    if ken_burns or transitions:
        # Advanced assembly with effects
        print("Using advanced assembly with effects...")
        success = assemble_with_effects(
            images, audio_file, output_file, calc_duration,
            transitions, ken_burns, transition_duration, srt_file, font_size
        )
    else:
        # Simple assembly
        print("Using simple assembly...")
        success = assemble_simple(images, audio_file, output_file, calc_duration, srt_file, font_size)
    
    # Cleanup
    if srt_file and os.path.exists(srt_file):
        os.remove(srt_file)
    
    return success

def assemble_with_effects(images, audio_file, output_file, duration_per_image,
                         transitions, ken_burns, trans_duration, srt_file, font_size):
    """Assemble video with Ken Burns and/or transitions using complex filtergraph."""
    
    n = len(images)
    fps = 30
    frame_count = int(duration_per_image * fps)
    
    # Build FFmpeg command with complex filtergraph
    inputs = []
    for img in images:
        inputs.extend(["-loop", "1", "-t", str(duration_per_image + (trans_duration if transitions else 0)), "-i", img])
    inputs.extend(["-i", audio_file])
    
    # Build filter complex
    filter_parts = []
    
    for i in range(n):
        if ken_burns:
            # Apply Ken Burns effect
            kb_filter = get_ken_burns_filter(i, duration_per_image + (trans_duration if transitions else 0))
            filter_parts.append(f"[{i}:v]{kb_filter},setsar=1[v{i}]")
        else:
            # Just scale and set duration
            filter_parts.append(f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps}[v{i}]")
    
    if transitions and n > 1:
        # Apply crossfade transitions between clips
        trans_frames = int(trans_duration * fps)
        
        # First transition
        filter_parts.append(f"[v0][v1]xfade=transition=fade:duration={trans_duration}:offset={duration_per_image - trans_duration}[vt1]")
        
        # Subsequent transitions
        for i in range(2, n):
            offset = (duration_per_image - trans_duration) * i
            filter_parts.append(f"[vt{i-1}][v{i}]xfade=transition=fade:duration={trans_duration}:offset={offset}[vt{i}]")
        
        final_video = f"[vt{n-1}]"
    else:
        # Just concatenate
        concat_inputs = "".join([f"[v{i}]" for i in range(n)])
        filter_parts.append(f"{concat_inputs}concat=n={n}:v=1:a=0[vout]")
        final_video = "[vout]"
    
    # Add subtitles if present
    if srt_file:
        srt_path = srt_file.replace("\\", "/").replace(":", "\\\\:")
        if transitions:
            filter_parts.append(f"{final_video}subtitles='{srt_path}':force_style='FontSize={font_size},FontName=Arial,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2,MarginV=50'[final]")
        else:
            filter_parts.append(f"{final_video}subtitles='{srt_path}':force_style='FontSize={font_size},FontName=Arial,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2,MarginV=50'[final]")
        final_video = "[final]"
    
    filter_complex = ";".join(filter_parts)
    
    # Build command
    cmd = ["ffmpeg", "-y"]
    cmd.extend(inputs)
    cmd.extend(["-filter_complex", filter_complex])
    cmd.extend(["-map", final_video.strip("[]") if not srt_file else "final"])
    cmd.extend(["-map", f"{n}:a"])
    cmd.extend(["-c:v", "libx264", "-pix_fmt", "yuv420p", "-shortest"])
    cmd.append(output_file)
    
    print("Running FFmpeg with advanced effects...")
    print(f"This may take several minutes for {n} images with effects...")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Successfully created video: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed: {e}")
        # Try simplified approach
        print("Trying simplified Ken Burns approach...")
        return assemble_ken_burns_simple(images, audio_file, output_file, duration_per_image, srt_file, font_size)

def assemble_ken_burns_simple(images, audio_file, output_file, duration_per_image, srt_file, font_size, 
                               add_intro=False, add_outro=False, watermark="Suscríbete"):
    """Simplified Ken Burns assembly with watermark support."""
    
    import tempfile
    temp_dir = tempfile.mkdtemp()
    temp_videos = []
    
    print("Processing images with Ken Burns effect (maintaining aspect ratio)...")
    
    for i, img in enumerate(images):
        temp_output = os.path.join(temp_dir, f"clip_{i:03d}.mp4")
        
        # Create a 16:9 canvas first, then apply Ken Burns
        d = int(duration_per_image * 30)
        
        # Alternating zoom effects - gentler zoom for better quality
        if i % 3 == 0:
            zoom_expr = "z='min(zoom+0.0008,1.2)'"
            x_expr = "x='iw/2-(iw/zoom/2)'"
            y_expr = "y='ih/2-(ih/zoom/2)'"
        elif i % 3 == 1:
            zoom_expr = "z='if(lte(zoom,1.0),1.2,max(1.001,zoom-0.0008))'"
            x_expr = "x='iw/2-(iw/zoom/2)'"
            y_expr = "y='ih/2-(ih/zoom/2)'"
        else:
            zoom_expr = "z='min(zoom+0.0005,1.1)'"
            x_expr = "x='if(lte(on,1),iw/4,min(x+1,iw*3/4))'" 
            y_expr = "y='ih/2-(ih/zoom/2)'"
        
        filter_str = (
            f"scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
            f"scale=3840:2160,"
            f"zoompan={zoom_expr}:{x_expr}:{y_expr}:d={d}:s=1920x1080:fps=30"
        )
        
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", img,
            "-vf", filter_str,
            "-t", str(duration_per_image),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            temp_output
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        temp_videos.append(temp_output)
        print(f"  Processed {i+1}/{len(images)}", end="\r")
    
    print(f"\nConcatenating {len(temp_videos)} clips...")
    
    # Create concat list
    list_file = os.path.join(temp_dir, "concat_list.txt")
    with open(list_file, "w") as f:
        for vid in temp_videos:
            f.write(f"file '{vid}'\n")
    
    # Build final video filter with subtitles and watermark
    vf_parts = []
    
    if srt_file:
        srt_path = srt_file.replace("\\", "/").replace(":", "\\\\:")
        vf_parts.append(f"subtitles='{srt_path}':force_style='FontSize={font_size},FontName=Arial,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2,MarginV=50'")
    
    if watermark and watermark.lower() not in ["none", "no", ""]:
        vf_parts.append(f"drawtext=text='{watermark}':fontsize=28:fontcolor=white@0.8:x=w-text_w-30:y=h-text_h-30:shadowcolor=black@0.6:shadowx=2:shadowy=2")
    
    # Final assembly with audio
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-i", audio_file]
    
    if vf_parts:
        cmd.extend(["-vf", ",".join(vf_parts)])
    
    cmd.extend(["-c:v", "libx264", "-pix_fmt", "yuv420p", "-shortest", output_file])
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Successfully created video: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed: {e}")
        return False
    finally:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)

def assemble_simple(images, audio_file, output_file, duration_per_image, srt_file, font_size):
    """Simple assembly without effects."""
    images_dir = os.path.dirname(images[0])
    
    list_file_path = os.path.join(images_dir, "input_list.txt")
    with open(list_file_path, "w", encoding='utf-8') as f:
        for img in images:
            safe_path = os.path.abspath(img).replace("\\", "/")
            f.write(f"file '{safe_path}'\n")
            f.write(f"duration {duration_per_image}\n")
        f.write(f"file '{os.path.abspath(images[-1]).replace(chr(92), '/')}'\n")

    vf_filters = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2"
    
    if srt_file:
        srt_path = srt_file.replace("\\", "/").replace(":", "\\\\:")
        vf_filters += f",subtitles='{srt_path}':force_style='FontSize={font_size},FontName=Arial,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2,MarginV=50'"

    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", list_file_path,
        "-i", audio_file,
        "-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p",
        "-vf", vf_filters,
        "-shortest",
        output_file
    ]

    print("Running FFmpeg...")
    try:
        subprocess.run(cmd_ffmpeg, check=True)
        print(f"\n✅ Successfully created video: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed: {e}")
        return False
    finally:
        if os.path.exists(list_file_path):
            os.remove(list_file_path)

def calculate_images_needed(audio_file, seconds_per_image):
    """Calculate how many images are needed."""
    duration = get_audio_duration(audio_file)
    if duration:
        import math
        num_images = math.ceil(duration / seconds_per_image)
        print(f"Audio: {duration:.2f}s | Image duration: {seconds_per_image}s | Images needed: {num_images}")
        return num_images
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create music videos with advanced effects.")
    parser.add_argument("--images_dir", default=None, help="Directory with images")
    parser.add_argument("--audio_file", required=True, help="Path to audio file")
    parser.add_argument("--output", default="output_video.mp4", help="Output filename")
    parser.add_argument("--image_duration", type=float, default=None, help="Seconds per image")
    parser.add_argument("--lyrics", default=None, help="Path to lyrics for subtitles")
    parser.add_argument("--font_size", type=int, default=48, help="Subtitle font size")
    parser.add_argument("--transitions", action="store_true", help="Enable crossfade transitions")
    parser.add_argument("--ken_burns", action="store_true", help="Enable Ken Burns zoom/pan effect")
    parser.add_argument("--transition_duration", type=float, default=1.0, help="Transition duration in seconds")
    parser.add_argument("--title", default=None, help="Video title for intro/outro (default: output filename)")
    parser.add_argument("--no_intro", action="store_true", help="Disable intro title card")
    parser.add_argument("--no_outro", action="store_true", help="Disable outro title card")
    parser.add_argument("--watermark", default="Suscríbete", help="Watermark text (empty to disable)")
    parser.add_argument("--calc", action="store_true", help="Only calculate images needed")
    
    args = parser.parse_args()
    
    if args.calc and args.image_duration:
        calculate_images_needed(args.audio_file, args.image_duration)
    elif args.images_dir:
        # Override song name with title if provided
        if args.title:
            # Patch the get_song_name_from_file function result
            original_func = get_song_name_from_file
            get_song_name_from_file = lambda x: args.title
        
        assemble_video_advanced(
            args.images_dir, 
            args.audio_file, 
            args.output,
            args.image_duration,
            args.lyrics,
            args.font_size,
            args.transitions,
            args.ken_burns,
            args.transition_duration
        )
    else:
        print("Error: --images_dir is required unless using --calc mode")

