# Mobile Battery & Interaction Audit

**Scope:** Android/Capacitor mobile build only  
**Status:** Source-level audit complete; physical-device battery testing is still required before release.

## What was verified

- The app manifest declares only `INTERNET`. It has no wake-lock, foreground-service, alarm, notification, location, camera, microphone, or broad-storage permission.
- There are no Android background services, scheduled workers, or background sync loops in the app code.
- The only recurring web timers in the mobile runtime are now paused whenever the app is not visible:
  - Performance diagnostics run only after the user starts a troubleshooting recording; their one-second monitor stops on background/page exit.
  - The study screen's "Learning Cards Due Soon" countdown pauses in the background and restarts only when the app becomes active again.
- Repeated UI taps reuse a small audio pool instead of creating a new audio object for every sound. Haptic feedback is light, shorter, and rate-limited so rapid selections do not queue vibrations.
- Animation work is event-driven (card swipe, flip, progress, loading) rather than a permanent animation loop. Both mobile screens now respect the device's **Reduce motion** accessibility setting.

## Interaction polish completed

- A deck row no longer presses, long-presses, or opens when its pin, Edit, Study, or other embedded control is tapped.
- Press feedback was reduced from an overly strong 0.93 scale to 0.97, making controls feel responsive without visually jumping.
- The performance report remains available, but is tucked into **Troubleshooting & diagnostics**, is off by default, and describes its privacy boundary in plain language.

## Physical-device release checks

1. Use the app for 15 minutes in Library, Create, and Study screens. It should remain responsive and should not become noticeably warm.
2. Leave the app on the countdown screen, background it for 10 minutes, then return. The timer must update correctly without having continued background work.
3. Leave the app in the background for at least 30 minutes and compare Android's per-app battery use with normal baseline use.
4. Turn on Android **Remove animations** / **Reduce motion** and confirm the app remains usable without movement-dependent cues.
5. Confirm sound and haptics can be disabled, and that rapid taps do not produce a buzzing or overlapping-click effect.

## Remaining scope

Onboarding, app identity assets, and opt-in study reminders are separate product work. Do not add notification permission until a reminder flow exists and a user has chosen to enable it.
