import os
import sys

# On macOS, Homebrew installs native libraries outside the default linker path.
# Add the Homebrew library directory first so WeasyPrint can load GLib/Pango.
if sys.platform == "darwin":
    for candidate in ("/opt/homebrew/lib", "/usr/local/lib"):
        if os.path.isdir(candidate):
            for key in ("DYLD_LIBRARY_PATH", "DYLD_FALLBACK_LIBRARY_PATH"):
                current = os.environ.get(key, "")
                os.environ[key] = candidate if not current else f"{candidate}{os.pathsep}{current}"
            break

from weasyprint import HTML

# Ensure output directory exists
os.makedirs("generated", exist_ok=True)

# 1. Generate core collection of 100 structured candidate entries
candidates = []
for i in range(1, 101):
    candidates.append({
        "rank": i,
        "roll_no": f"EX2026{i:04d}",
        "name": f"Candidate Name {i}",
        "score": round(100 - (i - 1) * 0.45, 2),
        "status": "Qualified" if i <= 60 else "Waiting List"
    })

# 2. Open standard document skeleton and style components
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
        color: #1e3a8a;
        margin-bottom: 5px;
        font-size: 22pt;
    }
    h2 {
        text-align: center;
        color: #0d9488;
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 16pt;
        border-bottom: 2px solid #0d9488;
        padding-bottom: 8px;
    }
    .page-block {
        page-break-after: always;
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
        border: 1px solid #e2e8f0;
        padding: 12px 14px;
        text-align: left;
    }
    th {
        background-color: #1e3a8a;
        color: white;
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

# 3. Process exactly 10 chunks to create distinct Officer Grade pages
chunk_size = 10
for page_num in range(10):
    start_idx = page_num * chunk_size
    end_idx = start_idx + chunk_size
    page_candidates = candidates[start_idx:end_idx]
    
    # Dynamically format the Grade designation title
    grade_title = f"Officer Grade {page_num + 1}"
    
    html_content += f"""
    <div class="page-block">
        <h1>Competitive Examination Results 2026</h1>
        <h2>Classification: {grade_title} (Ranks {start_idx + 1} - {end_idx})</h2>
        <table>
            <thead>
                <tr>
                    <th class="text-center" style="width: 12%;">Rank</th>
                    <th style="width: 23%;">Roll Number</th>
                    <th style="width: 35%;">Candidate Name</th>
                    <th class="text-center" style="width: 15%;">Score</th>
                    <th class="text-center" style="width: 15%;">Status</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for c in page_candidates:
        status_color = "#16a34a" if c['status'] == "Qualified" else "#d97706"
        html_content += f"""
                <tr>
                    <td class="text-center"><strong>{c['rank']}</strong></td>
                    <td>{c['roll_no']}</td>
                    <td>{c['name']}</td>
                    <td class="text-center">{c['score']}%</td>
                    <td class="text-center" style="color: {status_color}; font-weight: bold;">{c['status']}</td>
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

# 4. Generate the structured PDF report
output_pdf_path = "generated/classified_officer_ranks.pdf"
HTML(string=html_content).write_pdf(output_pdf_path)
print("PDF Layout Generated Successfully.")
