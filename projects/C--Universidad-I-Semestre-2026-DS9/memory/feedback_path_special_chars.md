# Special chars in project paths → rename immediately

If Next.js/Turbopack/webpack fails and the project path has `#` (or `%`, or other URL-special chars), stop analyzing and fix the path first:
1. Rename the folder to remove the special char
2. Or create a Windows junction at a clean path
3. Do NOT spend tokens reading stack traces — the fix is always the same.