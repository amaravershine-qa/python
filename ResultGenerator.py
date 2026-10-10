import os
import sys

# macOS Homebrew installs many native libraries outside the default linker path.
# WeasyPrint needs those libraries at import time, so configure the path first.
if sys.platform == "darwin":
    for candidate in ("/opt/homebrew/lib", "/usr/local/lib"):
        if os.path.isdir(candidate):
            for key in ("DYLD_LIBRARY_PATH", "DYLD_FALLBACK_LIBRARY_PATH"):
                existing = os.environ.get(key, "")
                value = candidate if not existing else f"{candidate}{os.pathsep}{existing}"
                os.environ[key] = value
            break

from weasyprint import HTML

# Ensure output directory exists
os.makedirs("generated", exist_ok=True)

# 1. Generate sample data for 100 mock candidates
candidates = []
for i in range(1, 101):
    candidates.append({
        "rank": i,
        "roll_no": f"EX2026{i:04d}",
        "name": f"Candidate Name {i}",
        "score": round(100 - (i - 1) * 0.45, 2),
        "status": "Qualified" if i <= 60 else "Waiting List"
    })

# 2. Build the HTML template with structural layout rules to guarantee exactly 10 pages
html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {
        size: A4;
        margin: 20mm;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-family: Arial, sans-serif;
            font-size: 10pt;
            color: #555;
        }
    }
    body {
        font-family: Arial, sans-serif;
        color: #333;
        margin: 0;
    }
    h1 {
        text-align: center;
        color: #1a365d;
        margin-bottom: 20px;
        font-size: 20pt;
    }
    .page-block {
        page-break-after: always;
        height: 100%;
    }
    .page-block:last-child {
        page-break-after: avoid;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    th, td {
        border: 1px solid #cbd5e1;
        padding: 10px 12px;
        text-align: left;
        font-size: 11pt;
    }
    th {
        background-color: #1a365d;
        color: white;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f8fafc;
    }
    .text-center {
        text-align: center;
    }
</style>
</head>
<body>
"""

# 3. Chunk the dataset sequentially (10 candidates per page across 10 pages)
chunk_size = 10
for page_num in range(10):
    start_idx = page_num * chunk_size
    end_idx = start_idx + chunk_size
    page_candidates = candidates[start_idx:end_idx]
    
    html_content += f"""
    <div class="page-block">
        <h1>Competitive Examination Results 2026</h1>
        <h3 style="color: #475569; border-bottom: 2px solid #1a365d; padding-bottom: 5px;">
            Rank List — Section {page_num + 1}
        </h3>
        <table>
            <thead>
                <tr>
                    <th class="text-center" style="width: 10%;">Rank</th>
                    <th style="width: 20%;">Roll Number</th>
                    <th style="width: 40%;">Candidate Name</th>
                    <th class="text-center" style="width: 15%;">Score</th>
                    <th class="text-center" style="width: 15%;">Status</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for c in page_candidates:
        html_content += f"""
                <tr>
                    <td class="text-center"><strong>{c['rank']}</strong></td>
                    <td>{c['roll_no']}</td>
                    <td>{c['name']}</td>
                    <td class="text-center">{c['score']}%</td>
                    <td class="text-center" style="color: {'#16a34a' if c['status'] == 'Qualified' else '#d97706'}">
                        {c['status']}
                    </td>
                </tr>
        """
        
    html_content += """
            </tbody>
        </table>
    </div>
    """

html_content += """
</body>
</html>
"""

# 4. Compile the HTML payload directly into the final PDF document
output_pdf_path = "generated/competitive_exam_ranks.pdf"
HTML(string=html_content).write_pdf(output_pdf_path)
print(f"Successfully generated PDF at: {output_pdf_path}")
