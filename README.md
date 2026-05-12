# rohanjames.dev — Portfolio Site

Personal portfolio for Rohan James. Live at [rohanjames.dev](https://rohanjames.dev).

---

## Stack

| Layer | Service |
|---|---|
| Static hosting | AWS S3 (`rohanjames.dev` bucket) |
| CDN + HTTPS | AWS CloudFront (`E15OXV0P8XZ4Y7`) |
| Media (MP3s + covers) | AWS S3 (`rohanjames-media` bucket) |
| Media CDN | AWS CloudFront (`d3vv8qd0hr1282.cloudfront.net`) |
| DNS | AWS Route 53 (`rohanjames.dev`) |
| SSL | AWS ACM cert (`526d8880-f607-4f77-9657-dcf4fc031450`, us-east-1) |
| Audio playback | Browser-native Audio API |

---

## Repo Structure

```
rohanjames-portfolio/
├── template_v3.html    # Source template — edit this
├── build_v3.py         # Build script — run this to generate index.html
├── index.html          # Built output — upload this to S3
└── README.md
```

> Photos are embedded as base64 directly in `index.html`.  
> MP3s and album covers live in the `rohanjames-media` S3 bucket, served via CloudFront.

---

## Making Changes

1. Edit `template_v3.html`
2. Run the build script:
   ```bash
   python3 build_v3.py
   ```
3. This outputs `rohanjames.html` — rename it to `index.html`
4. Upload `index.html` to S3 bucket `rohanjames.dev`
5. Invalidate CloudFront cache:
   - Go to CloudFront → Distribution `E15OXV0P8XZ4Y7` → Invalidations
   - Create invalidation with path `/*`
6. Hard refresh browser: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)

---

## AWS Resources

### S3 Buckets
- `rohanjames.dev` — static site (index.html)
- `rohanjames-media` — MP3s and cover art

### CloudFront Distributions
- Site: `d3kjk3yse2xxl.cloudfront.net` → distribution `E15OXV0P8XZ4Y7`
- Media: `d3vv8qd0hr1282.cloudfront.net`

### Route 53
- `rohanjames.dev` → A record (alias to CloudFront)
- `www.rohanjames.dev` → A record (alias to CloudFront)

### ACM Certificate
- ID: `526d8880-f607-4f77-9657-dcf4fc031450`
- Region: `us-east-1`
- Covers: `rohanjames.dev` + `www.rohanjames.dev`

### IAM User
- Username: `rjay`
- Account: `900466921705`

---

## Media Assets (S3 — rohanjames-media)

### Tracks
| File | CloudFront URL |
|---|---|
| chai-time.mp3 | https://d3vv8qd0hr1282.cloudfront.net/chai-time.mp3 |
| irani-cafe.mp3 | https://d3vv8qd0hr1282.cloudfront.net/irani-cafe.mp3 |
| lake-on-mars.mp3 | https://d3vv8qd0hr1282.cloudfront.net/lake-on-mars.mp3 |
| shadow.mp3 | https://d3vv8qd0hr1282.cloudfront.net/shadow.mp3 |
| traffic.mp3 | https://d3vv8qd0hr1282.cloudfront.net/traffic.mp3 |
| again.mp3 | https://d3vv8qd0hr1282.cloudfront.net/again.mp3 |

### Covers
| File | CloudFront URL |
|---|---|
| chai-time.png | https://d3vv8qd0hr1282.cloudfront.net/chai-time.png |
| irani-cafe.png | https://d3vv8qd0hr1282.cloudfront.net/irani-cafe.png |
| lake-on-mars.png | https://d3vv8qd0hr1282.cloudfront.net/lake-on-mars.png |
| shadow.jpg | https://d3vv8qd0hr1282.cloudfront.net/shadow.jpg |
| traffic.png | https://d3vv8qd0hr1282.cloudfront.net/traffic.png |
| again.jpg | https://d3vv8qd0hr1282.cloudfront.net/again.jpg |

---

## Updating Media

To add a new track:
1. Upload MP3 to `rohanjames-media` S3 bucket
2. Upload cover art to `rohanjames-media` S3 bucket
3. In `template_v3.html`, add a new entry to the `TRACKS` array:
   ```js
   {title: 'track name', src: 'https://d3vv8qd0hr1282.cloudfront.net/track-name.mp3', cover: 'https://d3vv8qd0hr1282.cloudfront.net/track-name.jpg'},
   ```
4. Rebuild and deploy (see Making Changes above)

---

## Swapping the Profile Photo

1. Get the new photo ready (square crop works best)
2. Drop it into the `/home/claude/photos/` directory as `profile_pic.jpg`
3. Run `python3 build_v3.py`
4. Deploy `index.html` to S3 + invalidate CloudFront

---

## Site Sections

- **About** — Bio, experience, skills. Content lives in `template_v3.html` around line 470+
- **Music** — Lofi player with 6 tracks. TRACKS array around line 651
- **Photography** — 14 street photos embedded as base64. Photos directory: `/home/claude/photos/`
