---
name: n8n API Key Rotator Builder
description: Create cascading API key rotator sub-workflows in n8n that automatically cycle through multiple API keys when one fails (403, rate limit) or returns empty data. Battle-tested pattern with zero sandbox issues.
---

# n8n API Key Rotator Builder

## Overview
This skill creates a **cascading API key rotator** sub-workflow in n8n. The rotator tries API keys one by one (Key 1 → Key 2 → ... → Key N) until one succeeds with real data. It handles:
- **403 errors** (rate limited / quota exceeded)
- **Empty responses** (API returns `[]` with no data)
- **Network errors** (timeouts, 500s)
- **Any HTTP error** that n8n catches

## ⚠️ CRITICAL RULES - Read Before Building

### Things that DO NOT work in n8n (learned the hard way):
1. **`fetch()` is BLOCKED** in n8n Code nodes (sandbox restriction)
2. **`require('https')` is BLOCKED** in n8n Code nodes
3. **`AbortController` is BLOCKED** in n8n Code nodes
4. **`$getWorkflowStaticData()` does NOT persist** reliably across sub-workflow calls
5. **SplitInBatches loops** are unreliable for retry patterns in execution order v1
6. **HTTP Request with empty array response `[]`** produces 0 output items — downstream nodes NEVER execute unless you set `alwaysOutputData: true`

### Things that DO work:
1. ✅ **Native HTTP Request nodes** with `onError: "continueRegularOutput"`
2. ✅ **Native IF nodes** for checking success/failure
3. ✅ **`alwaysOutputData: true`** on HTTP Request nodes to prevent dead flows
4. ✅ **Cascading pattern** (Key1 → Check → Key2 → Check → ... → KeyN)
5. ✅ **Expression references** like `$('Prepare Input').first().json.apiBody`

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     ROTATOR SUB-WORKFLOW                                │
│                                                                         │
│  Trigger → Prepare Input → Call Key 1 → Check Key 1                    │
│                                 │            │                          │
│                                 │      ┌─────┴─────┐                   │
│                                 │   TRUE(data)  FALSE(error/empty)     │
│                                 │      │            │                   │
│                                 │  Return Success   Call Key 2          │
│                                 │      ▲            │                   │
│                                 │      │      Check Key 2               │
│                                 │      │       │         │              │
│                                 │      │    TRUE      FALSE             │
│                                 │      │       │         │              │
│                                 │      └───────┘    Call Key 3          │
│                                 │      ▲             ...                │
│                                 │      └─── (pattern repeats) ──→ Key N│
└─────────────────────────────────────────────────────────────────────────┘
```

## Step-by-Step: Building a New Rotator

### Step 1: Create the workflow using n8n MCP

Use `mcp_n8n-mcp_n8n_create_workflow` with this structure.

### Step 2: Define the nodes

You need these node types for N keys:
- 1× `executeWorkflowTrigger` (Trigger)
- 1× `code` (Prepare Input)
- N× `httpRequest` (Call Key 1..N)
- N× `if` (Check Key 1..N)
- 1× `code` (Return Success)
- 1× `stickyNote` (Documentation)

### Step 3: Node Configurations

#### Trigger Node
```json
{
  "id": "trigger-rotator",
  "name": "Trigger - Rotator Start",
  "type": "n8n-nodes-base.executeWorkflowTrigger",
  "typeVersion": 1.1,
  "position": [0, 0],
  "parameters": {
    "inputSource": "jsonExample",
    "jsonExample": "{\n  \"actorUrl\": \"https://api.example.com/endpoint\",\n  \"apiBody\": {}\n}"
  }
}
```

#### Prepare Input Node
```json
{
  "id": "code-prepare",
  "name": "Prepare Input",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [220, 0],
  "parameters": {
    "jsCode": "const input = $input.first().json;\nreturn [{ json: { actorUrl: input.actorUrl, apiBody: input.apiBody } }];"
  }
}
```

#### HTTP Request Node (Call Key N) - ⚠️ CRITICAL CONFIG
```json
{
  "id": "http-keyN",
  "name": "Call Key N",
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4.2,
  "position": [440 + (N-1)*220, (N-1)*120],
  "onError": "continueRegularOutput",
  "alwaysOutputData": true,
  "parameters": {
    "url": "={{ $('Prepare Input').first().json.actorUrl }}",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {
          "name": "Authorization",
          "value": "Bearer YOUR_API_KEY_N_HERE"
        }
      ]
    },
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={{ JSON.stringify($('Prepare Input').first().json.apiBody) }}",
    "options": {
      "timeout": 300000,
      "redirect": { "redirect": { "followRedirects": true } },
      "response": { "response": { "responseFormat": "json" } }
    }
  }
}
```

**⚠️ MANDATORY properties on each HTTP Request node:**
- `"onError": "continueRegularOutput"` — Prevents workflow crash on HTTP errors
- `"alwaysOutputData": true` — Prevents dead flow when API returns empty `[]`

**NOTE for Key 1:** Use `$json.actorUrl` and `$json.apiBody` (direct reference).
**NOTE for Keys 2+:** Use `$('Prepare Input').first().json.actorUrl` (named reference back to Prepare Input).

#### IF Node (Check Key N) - ⚠️ CRITICAL CONDITION
```json
{
  "id": "if-keyN",
  "name": "Check Key N",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2.2,
  "position": [660 + (N-1)*220, (N-1)*120],
  "parameters": {
    "conditions": {
      "combinator": "and",
      "conditions": [
        {
          "id": "cN",
          "leftValue": "={{ (!$json.error && Object.keys($json).length > 0) ? 'yes' : 'no' }}",
          "operator": {
            "operation": "equals",
            "type": "string"
          },
          "rightValue": "yes"
        }
      ],
      "options": {
        "caseSensitive": true,
        "leftValue": "",
        "typeValidation": "strict",
        "version": 2
      }
    }
  }
}
```

**The condition `(!$json.error && Object.keys($json).length > 0)` handles 3 cases:**
| Scenario | `$json` value | Condition result | Route |
|----------|---------------|------------------|-------|
| Error (403, 500, etc.) | `{error: {...}}` | `!{...} = false` → `'no'` | FALSE → next key |
| Empty response `[]` | `{}` | `Object.keys({}).length = 0` → `'no'` | FALSE → next key |
| Real data | `{title: "...", ...}` | `true && true` → `'yes'` | TRUE → Return Success |

#### Return Success Node
```json
{
  "id": "code-return-success",
  "name": "Return Success",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [1760, -120],
  "parameters": {
    "jsCode": "const items = $input.all();\nreturn items;"
  }
}
```

### Step 4: Define connections

```
Trigger → Prepare Input → Call Key 1 → Check Key 1
                                          ├── TRUE [index 0] → Return Success
                                          └── FALSE [index 1] → Call Key 2 → Check Key 2
                                                                                ├── TRUE → Return Success
                                                                                └── FALSE → Call Key 3 → ...
```

Connection pattern for each Check Key N:
```json
"Check Key N": {
  "main": [
    [{"index": 0, "node": "Return Success", "type": "main"}],
    [{"index": 0, "node": "Call Key N+1", "type": "main"}]
  ]
}
```

For the LAST Check Key, the FALSE output is empty:
```json
"Check Key LAST": {
  "main": [
    [{"index": 0, "node": "Return Success", "type": "main"}],
    []
  ]
}
```

### Step 5: Workflow settings

```json
{
  "executionOrder": "v1",
  "callerPolicy": "workflowsFromSameOwner",
  "availableInMCP": false
}
```

## How to Call the Rotator from a Parent Workflow

### From a Code node (Prepare Request):
```javascript
const items = $input.all();
return items.map(item => ({
  json: {
    actorUrl: "https://api.example.com/v2/endpoint",
    apiBody: {
      query: item.json.searchQuery,
      limit: 100
    }
  }
}));
```

### From an Execute Workflow node:
- Set "Workflow" to the rotator's workflow ID
- Connect the Prepare Request code node's output to the Execute Workflow node

## Adapting for Different Auth Methods

### Bearer Token (most common - Apify, OpenAI, etc.)
```json
"headerParameters": {
  "parameters": [{"name": "Authorization", "value": "Bearer YOUR_KEY"}]
}
```

### API Key as Query Parameter (Hunter.io, Abstract API, etc.)
Change the URL to include the key:
```json
"url": "={{ $('Prepare Input').first().json.actorUrl + '?api_key=YOUR_KEY' }}"
```

### API Key as Custom Header (SendGrid, etc.)
```json
"headerParameters": {
  "parameters": [{"name": "X-Api-Key", "value": "YOUR_KEY"}]
}
```

### Basic Auth
```json
"headerParameters": {
  "parameters": [
    {"name": "Authorization", "value": "Basic BASE64_ENCODED_USER_PASS"}
  ]
}
```

## Quick Reference: Creating a 7-Key Rotator

When the user asks to create a new rotator, use this checklist:

1. [ ] Collect: API name, base URL, auth method, 7 API keys
2. [ ] Use `mcp_n8n-mcp_n8n_create_workflow` with all nodes
3. [ ] Set `onError: "continueRegularOutput"` on ALL HTTP Request nodes
4. [ ] Set `alwaysOutputData: true` on ALL HTTP Request nodes
5. [ ] Use the condition `(!$json.error && Object.keys($json).length > 0)` on ALL IF nodes
6. [ ] Key 1 references `$json.actorUrl`, Keys 2+ reference `$('Prepare Input').first().json.actorUrl`
7. [ ] All Check Keys TRUE output → Return Success
8. [ ] All Check Keys FALSE output → next Call Key (except last)
9. [ ] Set `callerPolicy: "workflowsFromSameOwner"` in settings
10. [ ] Test with at least one known-bad key to verify cascading works

## Debugging Tips

| Symptom | Cause | Fix |
|---------|-------|-----|
| Workflow stops after empty response | Missing `alwaysOutputData: true` | Add it to the HTTP Request node |
| Error crashes workflow | Missing `onError: "continueRegularOutput"` | Add it to the HTTP Request node |
| Key 2+ doesn't receive input data | Using `$json.actorUrl` instead of named ref | Use `$('Prepare Input').first().json.actorUrl` |
| Code node fails with "fetch not defined" | n8n sandbox blocks fetch | Use native HTTP Request nodes instead |
| SplitInBatches doesn't loop | Execution order v1 issue | Use cascading pattern instead of loops |
| All keys tried, no data | All accounts exhausted | Check dashboards, wait for monthly refresh |

## Example: Full 7-Key Rotator JSON Template

See the Apify Rotator workflow `pmgk2uIAZjzrCfnU` as the reference implementation.
To duplicate for a new API:
1. Get the workflow: `mcp_n8n-mcp_n8n_get_workflow` with id `pmgk2uIAZjzrCfnU`
2. Change all 7 API keys in the header parameters
3. Change the URL if the new API uses query param auth
4. Create as new workflow: `mcp_n8n-mcp_n8n_create_workflow`
5. Update the parent workflow to call the new rotator ID
