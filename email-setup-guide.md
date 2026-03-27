# Email Forwarding Setup — Cloudflare

Free email routing for professional outreach addresses.

## Domains to Set Up
- `clawprint.dev` → scott@clawprint.dev
- `nakamotodesign.co` → hello@nakamotodesign.co (if this domain is on Cloudflare)

## Steps (takes ~5 min per domain)

1. Log into Cloudflare dashboard
2. Select the domain (e.g., clawprint.dev)
3. Go to **Email** → **Email Routing**
4. Click **Get Started** (or **Enable Email Routing**)
5. Add a custom address:
   - Custom address: `scott` (or `hello`)
   - Forward to: `skb.rene@gmail.com`
6. Cloudflare will show required DNS records (MX + TXT) — click **Add records automatically**
7. Verify your Gmail receives the confirmation email, click confirm
8. Done. Emails to scott@clawprint.dev forward to Gmail.

## For Sending FROM the Custom Address (via Gmail)

1. In Gmail → Settings → Accounts → "Send mail as" → Add another email
2. Enter: scott@clawprint.dev
3. SMTP server: `smtp.gmail.com`, port 587
4. Username: your Gmail, password: app-specific password
5. Verify via confirmation email
6. Now you can send as scott@clawprint.dev from Gmail

## Why This Matters
- Cold emails from scott@clawprint.dev look way more professional than Gmail
- Free forever on Cloudflare
- No new inbox to manage — everything funnels to Gmail

## Action Required
Scott needs to do this — requires Cloudflare login.
