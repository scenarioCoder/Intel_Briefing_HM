import os
import json
from datetime import datetime

# Define the root directory for reports
REPORTS_DIR = "reports"
OUTPUT_FILE = os.path.join(REPORTS_DIR, "index.json")

# Category mapping for better display names
CATEGORY_NAMES = {
    "daily_briefings": "📊 情报日报",
    "tactical": "💰 赏金猎人",
    "web3": "⛏️ Alpha 雷达",
    "opportunities": "🏗️ 营收分析"
}

def build_index():
    index_data = {
        "last_updated": datetime.now().isoformat(),
        "categories": []
    }

    if not os.path.exists(REPORTS_DIR):
        print(f"Warning: '{REPORTS_DIR}' directory does not exist.")
        return index_data

    # Scan directories in reports/
    for category_folder in os.listdir(REPORTS_DIR):
        category_path = os.path.join(REPORTS_DIR, category_folder)
        
        # Only process directories, skip files like index.json
        if not os.path.isdir(category_path):
            continue
            
        category_info = {
            "id": category_folder,
            "name": CATEGORY_NAMES.get(category_folder, category_folder),
            "files": []
        }
        
        # Scan markdown files in category
        for filename in os.listdir(category_path):
            if filename.endswith(".md"):
                file_path = os.path.join(category_path, filename)
                # Get basic file stats
                stat = os.stat(file_path)
                
                # Try to extract a nice title from the filename (e.g. Morning_Report_2026-03-10.md -> 2026-03-10)
                display_title = filename.replace(".md", "")
                if "_" in display_title:
                    parts = display_title.split("_")
                    if len(parts) > 1:
                        # Extract date part if it looks like Morning_Report_YYYY-MM-DD
                        display_title = parts[-1]
                
                category_info["files"].append({
                    "filename": filename,
                    "title": display_title,
                    "path": f"{category_folder}/{filename}",
                    "date": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size": stat.st_size
                })
                
        # Sort files chronologically descending (newest first)
        category_info["files"].sort(key=lambda x: x["date"], reverse=True)
        
        # Only add category if it has files
        if category_info["files"]:
            index_data["categories"].append(category_info)

    # Sort categories alphabetically mostly to keep consistent order
    index_data["categories"].sort(key=lambda x: x["id"])

    # Write the JSON output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Successfully built report index with {sum(len(c['files']) for c in index_data['categories'])} files across {len(index_data['categories'])} categories.")
    print(f"📄 Output saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_index()
