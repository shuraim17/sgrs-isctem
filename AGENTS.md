
## Supabase Migration (May 2026)
- The project has been migrated from Firebase to Supabase.
- **Project URL:** https://exooykvgjxckvcnxhiap.supabase.co
- **Database:** PostgreSQL with Row Level Security (RLS).
- **Authentication:** Supabase Auth (Email/Password).
- **Notifications:** Handled via Supabase Edge Function `notifications` (integrates Twilio).
- **Standard Credentials:**
  - admin@isctem.ac.mz / admin123
  - gestor@isctem.ac.mz / gestor123
  - docente@isctem.ac.mz / docente123
- **Admin Key:** `isctem2026admin` (verified via DB function `check_admin_key`).
- **Real-time:** Uses Supabase Realtime (PubSub) for dashboard updates.
