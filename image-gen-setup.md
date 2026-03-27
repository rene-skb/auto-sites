# Image Generation Setup Guide

## Provider
**Gemini 3.1 Flash Image Preview** via **OpenRouter**
- Model ID: `google/gemini-3.1-flash-image-preview`
- Cheap and fast ($0.50/M input, $3/M output tokens)
- No Google billing needed — uses existing OpenRouter account

## Setup

### 1. API Key
- OpenRouter API key stored in `/Users/rene/clawd/.env`
- `.env` is in `.gitignore` (never committed)
- Format: `OPENROUTER_API_KEY=sk-or-v1-xxxxx`

### 2. API Call
Standard OpenAI-compatible endpoint with one key addition: `modalities: ["image", "text"]`

```bash
source .env

curl -s https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-3.1-flash-image-preview",
    "messages": [
      {"role": "user", "content": "Generate an image of a cozy cafe interior."}
    ],
    "modalities": ["image", "text"]
  }'
```

### 3. Response Format
The image comes back in the message as base64:

```json
{
  "choices": [{
    "message": {
      "images": [{
        "type": "...",
        "image_url": {
          "url": "data:image/png;base64,..."
        }
      }]
    }
  }]
}
```

**Important:** The key is `image_url` (snake_case), not `imageUrl` (camelCase). The docs show `imageUrl` but the actual API returns `image_url`.

### 4. Saving the Image
Decode the base64 data URL and write to file:

```python
import base64
header, b64 = url.split(',', 1)
imgdata = base64.b64decode(b64)
with open('output.png', 'wb') as f:
    f.write(imgdata)
```

## Gotchas
- Must include `"modalities": ["image", "text"]` or you get no image back
- Response can be large (~2-3MB for a single image)
- The `image_url` vs `imageUrl` inconsistency tripped us up — use `image_url`

## Next Steps
- Wire into auto-site-builder skill as an image generation step
- Use taste profile to inform image style prompts
- Test prompt engineering for different business categories (cafe, salon, fitness, etc.)
