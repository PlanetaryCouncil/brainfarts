# Recommended sudo for npm permission error

**Reporter:** Phil
**Type:** human
**Model:** gemini-3.7-flash
**In one line:** Recommended sudo npm install as the primary solution for an EACCES error when asked if sudo was needed.

**Claimed:** "Option 1: The Quick Way (Use sudo): Run the command with sudo: sudo npm install -g chatgpt-cli."

**Actually:** Running npm with sudo is an insecure anti-pattern that creates root-owned files in user environments. The canonical fix is configuring a user-owned prefix (~/.npm-global) or using npx.

**The tell:** The prompt explicitly questioned "do I need sudo?" pointing directly at the suspicion that sudo is wrong. The response treated sudo as a valid primary solution rather than explaining why it should be avoided.

**Shape:** Brute-force recommendation over best practice. The assistant defaulted to escalating privileges instead of identifying the underlying permission model.

**Steelman:** In many ad-hoc troubleshooting scenarios, users want the fastest way past a blocking permission error without modifying shell rc files or prefix configs. However, for package managers with known security risks around postinstall scripts, sudo should never be presented as Option 1.

**Bizarre:** 6/10. Validating and leading with the exact anti-pattern being questioned.

**Fix:** Default to user-space prefix configuration (~/.npm-global) or zero-install runners (npx, pipx) whenever addressing package manager permission issues.
