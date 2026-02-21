---
name: music_video_creator
description: key_skill. Creates a music video from a song file and lyrics. It analyzes lyrics, generates prompts, creates images, and stitches them into a video using FFmpeg.
---

# Music Video Creator Skill

This skill creates music videos from an audio file and lyrics with customizable scene duration, synchronized subtitles, Ken Burns effects, and transitions.

## Prerequisites
- `ffmpeg` must be installed and in PATH

## Workflow

### Step 1: Analyze Requirements
Ask the user:
1. **Audio file** path
2. **Lyrics** (text or file)
3. **Visual style** (Realistic, Anime, Watercolor, Cyberpunk, etc.)
4. **Image duration** (default: 5 seconds per image)
5. **Include lyrics as subtitles?** (yes/no)
6. **Effects** (Ken Burns zoom, transitions)

### Step 2: Check Image Bank for Reusable Images
Before generating new images:
1. Read `Banco_Imagenes/index.json`
2. Search for images matching the new song's themes/keywords
3. Show user which existing images could be reused
4. Only generate what's missing

### Step 3: Calculate Images Needed
```bash
python .agent/skills/music_video_creator/scripts/video_assembler.py --audio_file "path/to/song.mp3" --image_duration 5 --calc
```

### Step 4: Generate Scene Prompts
For each scene, create a prompt based on lyrics segments:
- Format: `[Style] cinematic image of [scene description], high quality, dramatic lighting`

### Step 5: Generate Images
Use `generate_image` tool for EACH scene. Save to `_video_assets/scene_XX.jpg`

### Step 6: Update Image Bank
After generating images:
1. Copy new images to `Banco_Imagenes/` with song prefix (e.g., `NuevaCancion_scene_01.jpg`)
2. Update `Banco_Imagenes/index.json` with new entries including:
   - descripcion
   - keywords
   - cancion
   - estilo
   - verso

### Step 7: Create Lyrics File (if subtitles requested)
Save lyrics to `_video_assets/lyrics.txt`, one line per subtitle segment.

### Step 8: Assemble Video
Run the assembler with appropriate options:

**Basic:**
```bash
python .agent/skills/music_video_creator/scripts/video_assembler.py --images_dir "_video_assets" --audio_file "path/to/song.mp3" --output "video.mp4"
```

**With Ken Burns effect:**
```bash
python .agent/skills/music_video_creator/scripts/video_assembler.py --images_dir "_video_assets" --audio_file "path/to/song.mp3" --output "video.mp4" --ken_burns
```

**With subtitles:**
```bash
python .agent/skills/music_video_creator/scripts/video_assembler.py --images_dir "_video_assets" --audio_file "path/to/song.mp3" --output "video.mp4" --lyrics "_video_assets/lyrics.txt"
```

**Full options (Ken Burns + Subtitles):**
```bash
python .agent/skills/music_video_creator/scripts/video_assembler.py --images_dir "_video_assets" --audio_file "path/to/song.mp3" --output "video.mp4" --image_duration 5 --lyrics "_video_assets/lyrics.txt" --font_size 42 --ken_burns
```

## Script Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--images_dir` | Directory with scene images | Required |
| `--audio_file` | Path to audio file | Required |
| `--output` | Output video filename | output_video.mp4 |
| `--image_duration` | Seconds per image | Auto-fit to audio |
| `--lyrics` | Path to lyrics.txt for subtitles | None |
| `--font_size` | Subtitle font size | 48 |
| `--ken_burns` | Enable Ken Burns zoom/pan effect | False |
| `--transitions` | Enable crossfade transitions | False |
| `--transition_duration` | Transition duration in seconds | 1.0 |
| `--calc` | Only calculate images needed | False |

## Image Bank System

### Location
`frozen-mare/Banco_Imagenes/`

### Index File
`Banco_Imagenes/index.json` contains metadata for all images:
- `descripcion`: What the image shows
- `keywords`: Searchable tags
- `cancion`: Source song
- `estilo`: Visual style
- `verso`: Song section

### Reusing Images
When keywords match between new song lyrics and existing images:
1. Show matches to user
2. Get approval before reusing
3. Only generate truly new scenes
