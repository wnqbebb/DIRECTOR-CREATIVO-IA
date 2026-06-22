import json
import os

transcript_path = r"C:\Users\Admin\.gemini\antigravity-ide\brain\bd0c69fa-ba03-410c-9eed-a9e86dba0b77\.system_generated\logs\transcript.jsonl"
out_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\scratch\all_writes_summary.txt"

def clean_val(val):
    if not val:
        return ""
    val = val.strip()
    if val.startswith('"') and val.endswith('"'):
        try:
            return json.loads(val)
        except:
            return val[1:-1]
    return val

with open(transcript_path, "r", encoding="utf-8") as f, open(out_path, "w", encoding="utf-8") as out:
    for line in f:
        try:
            step = json.loads(line)
            idx = step.get("step_index")
            for call in step.get("tool_calls", []):
                name = call.get("name")
                args = call.get("args", {})
                target_raw = args.get("TargetFile", args.get("Target", ""))
                target = clean_val(target_raw)
                if not target:
                    continue
                if any(ext in target for ext in [".css", ".html", ".py", ".js"]):
                    content_raw = args.get("CodeContent", args.get("ReplacementContent", ""))
                    content = clean_val(content_raw)
                    summary = content.replace("\n", " ")[:120]
                    out.write(f"Step {idx}: {name} -> {target} | Length: {len(content)} | Content: {summary}...\n")
        except Exception as e:
            pass

print("Done! Summary written to", out_path)
