
---

### 📄 `contributor_notes.md`

```markdown
# 🛠 Contributor Notes — WEAVR

> "Scrolls are not shipped. They are summoned."

---

## Folder Rituals

- `agents/`: All operational logic lives here. Every agent must include:
  - `.sh`, `.scroll`, `.glyph`, `.env.sample`, `pipeline.yml`
- `docker/`: Every new stack must define its own compose file
- `scrolls/`: Holds scroll-based documentation, rituals, meta-processes
- `ui/`: Optional — embed dashboards, map interfaces, or feedback UIs

---

## Dev Rituals

| Action | Command |
|--------|---------|
| Build stack | `docker compose build` |
| Run stack | `docker compose up -d` |
| Shell into agent | `docker exec -it weavr_agent bash` |
| Export build | `zip -r ./output/weavr_stack.zip ./` |

---

## Sprint Cadence (Suggested)

- 🔁 Weekly scroll review (new stack concepts, failures)
- ✅ Feature lock every 3rd cycle
- 📜 Every agent must self-document in `.scroll`

---

## Meta

If you fork this for civic or commercial use — keep scroll naming conventions clear.  
WEAVR is not SaaS. It is scroll-as-infrastructure.

> Leave scrolls better than you found them.
