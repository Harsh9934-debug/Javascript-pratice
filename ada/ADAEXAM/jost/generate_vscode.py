import os
import json
import re

files = ["1st.py", "2nd.py", "3rd.py", "4th.py", "5th.py", "6th.py", 
         "7th.py", "8th.py", "9th.py", "10th.py", "11th.py", "12th.py"]

# Target directory - we check where we are running, but pull from ADAEXAM natively
base_path = "/Users/harsh/Desktop/JavascriptPratice/ada/ADAEXAM"
export_path = os.path.join(base_path, "jost", "all_programs.html")

file_data = {}
for f in files:
    path = os.path.join(base_path, f)
    # Check fallback path in case some were moved to pratice/ or jost/
    if not os.path.exists(path):
        alt_path = os.path.join(base_path, "pratice", f)
        if os.path.exists(alt_path):
            path = alt_path
            
    code = "File not found."
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            # Escape HTML tags before we do syntax highlighting
            code = file.read().replace('<', '&lt;').replace('>', '&gt;')
            
            # Very basic string check
            code = re.sub(r'(".+?")', r'<span class="string">\1</span>', code)
            code = re.sub(r"('.+?')", r'<span class="string">\1</span>', code)
            
            # Very basic syntax highlighting
            code = code.replace('def ', '<span class="keyword-blue">def</span> ')
            code = code.replace('class ', '<span class="keyword-blue">class</span> ')
            code = code.replace('if ', '<span class="keyword">if</span> ')
            code = code.replace('elif ', '<span class="keyword">elif</span> ')
            code = code.replace('else:', '<span class="keyword">else</span>:')
            code = code.replace('for ', '<span class="keyword">for</span> ')
            code = code.replace(' in ', ' <span class="keyword">in</span> ')
            code = code.replace('while ', '<span class="keyword">while</span> ')
            code = code.replace('return ', '<span class="keyword">return</span> ')
            code = code.replace('break', '<span class="keyword">break</span>\n')
            
            # Functions
            funcs = ['print', 'len', 'range', 'min', 'max', 'map', 'split', 'input', 'zip', 'sorted', 'all', 'sum', 'enumerate', 'next']
            for func in funcs:
                code = code.replace(func + '(', f'<span class="function">{func}</span>(')

    lines = code.split('\n')
    line_nums = "\n".join(str(i+1) for i in range(len(lines)))
    code_html = "\n".join(lines)
    
    file_data[f] = {
        "line_nums": line_nums,
        "code_html": code_html
    }

js_data = json.dumps(file_data)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADA_EXAM_PREP - Visual Studio Code</title>
    <style>
        body, html {{
            margin: 0; padding: 0; width: 100vw; height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #1e1e1e; color: #cccccc; overflow: hidden; display: flex; flex-direction: column;
        }}
        .top-bar {{ height: 30px; background-color: #3c3c3c; display: flex; align-items: center; justify-content: center; font-size: 13px; color: #cccccc; }}
        .main-container {{ display: flex; flex: 1; overflow: hidden; }}
        
        .activity-bar {{ width: 50px; background-color: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 15px; border-right: 1px solid #252526; }}
        .activity-icon {{ font-size: 20px; margin-bottom: 25px; opacity: 0.5; cursor: pointer; }}
        .activity-icon.active {{ opacity: 1; border-left: 2px solid white; padding-left: 2px; }}
        
        .sidebar {{ width: 250px; background-color: #252526; border-right: 1px solid #1e1e1e; display: flex; flex-direction: column; }}
        .sidebar-header {{ padding: 10px 20px; font-size: 11px; text-transform: uppercase; color: #858585; display: flex; justify-content: space-between; }}
        .sidebar-list {{ overflow-y: auto; flex: 1; padding-bottom: 20px; }}
        .file-item {{ padding: 4px 20px; cursor: pointer; font-size: 13px; display: flex; align-items: center; }}
        .file-item:hover {{ background-color: #2a2d2e; }}
        .file-item.active {{ background-color: #37373d; color: #ffffff; }}
        .file-icon {{ color: #519aba; margin-right: 6px; font-weight: bold; font-family: monospace; font-size: 15px; }}
        
        .editor-container {{ flex: 1; display: flex; flex-direction: column; background-color: #1e1e1e; }}
        
        .tabs {{ display: flex; background-color: #252526; height: 35px; border-bottom: 1px solid #1e1e1e; }}
        .tab {{ padding: 0 15px; display: flex; align-items: center; background-color: #1e1e1e; color: #ffffff; border-top: 2px solid #519aba; font-size: 13px; border-right: 1px solid #252526; cursor: default; }}
        
        .breadcrumbs {{ padding: 5px 15px; font-size: 12px; color: #858585; background-color: #1e1e1e; display:flex; align-items: center; border-bottom: 1px solid #1e1e1e; box-shadow: 0 1px 2px rgba(0,0,0,0.1);}}
        
        .code-area {{ display: flex; flex: 1; overflow: auto; padding-top: 10px; background-color: #1e1e1e; }}
        .line-numbers {{ padding: 0 15px 50px 15px; text-align: right; color: #858585; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.5; user-select: none; border-right: 1px solid #404040; margin:0 }}
        .code-content {{ padding: 0 15px 50px 15px; margin: 0; color: #d4d4d4; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; line-height: 1.5; tab-size: 4; white-space: pre; flex: 1; }}
        
        .status-bar {{ height: 22px; background-color: #007acc; display: flex; justify-content: space-between; align-items: center; padding: 0 10px; font-size: 12px; color: white; }}
        .status-item {{ margin-right: 15px; cursor: default; }}
        
        .keyword {{ color: #c586c0; }}
        .keyword-blue {{ color: #569cd6; }}
        .function {{ color: #dcdcaa; }}
        .string {{ color: #ce9178; }}
    </style>
</head>
<body>
    <div class="top-bar">ADA_EXAM_PREP - Visual Studio Code</div>
    <div class="main-container">
        <div class="activity-bar">
            <!-- Emulate VS Code icons -->
            <div class="activity-icon active">📄</div>
            <div class="activity-icon">🔍</div>
            <div class="activity-icon">⎇</div>
            <div class="activity-icon">🐞</div>
        </div>
        <div class="sidebar">
            <div class="sidebar-header">
                <span>Explorer</span>
                <span>...</span>
            </div>
            <div class="sidebar-header" style="color:#cccccc; cursor:none;">
                <span id="folderIcon">▼</span> ADA_EXAM_PREP
            </div>
            <div class="sidebar-list" id="fileList"></div>
        </div>
        <div class="editor-container">
            <div class="tabs">
                <div class="tab">
                    <span class="file-icon" style="font-size:12px;">Py</span>
                    <span id="activeTabName">1st.py</span>
                </div>
            </div>
            <div class="breadcrumbs">
                ADA_EXAM_PREP &gt; <span id="breadcrumbName" style="color:#cccccc; margin-left:5px;">1st.py</span>
            </div>
            <div class="code-area">
                <pre class="line-numbers" id="lineNumbers"></pre>
                <div class="code-content" id="codeContent"></div>
            </div>
        </div>
    </div>
    <div class="status-bar">
        <div>
            <span class="status-item">main*</span>
            <span class="status-item">0 ⚠ 0 ✖</span>
        </div>
        <div>
            <span class="status-item">Ln 1, Col 1</span>
            <span class="status-item">Spaces: 4</span>
            <span class="status-item">UTF-8</span>
            <span class="status-item" style="color:#ffffff;">Python</span>
        </div>
    </div>

    <script>
        // Data injected from Python
        const fileData = {js_data};
        const fileNames = Object.keys(fileData);
        let activeFile = fileNames[0];

        function renderSidebar() {{
            const list = document.getElementById('fileList');
            list.innerHTML = '';
            fileNames.forEach(f => {{
                const div = document.createElement('div');
                div.className = 'file-item' + (f === activeFile ? ' active' : '');
                div.innerHTML = `<span class="file-icon">Py</span> ${{f}}`;
                div.onclick = () => selectFile(f);
                list.appendChild(div);
            }});
        }}

        function selectFile(fileName) {{
            activeFile = fileName;
            document.getElementById('activeTabName').innerText = fileName;
            document.getElementById('breadcrumbName').innerText = fileName;
            
            let htmlData = fileData[fileName].code_html;
            if(htmlData === "File not found.") {{
                document.getElementById('lineNumbers').innerText = "1";
            }} else {{
                document.getElementById('lineNumbers').innerText = fileData[fileName].line_nums;
            }}
            
            document.getElementById('codeContent').innerHTML = htmlData;
            renderSidebar();
        }}
        
        // Init
        if (fileNames.length > 0) {{
            selectFile(activeFile);
        }}
    </script>
</body>
</html>
"""

os.makedirs(os.path.dirname(export_path), exist_ok=True)
with open(export_path, "w", encoding="utf-8") as out:
    out.write(html_template)
print("Interactive VS Code clone HTML created successfully.")
