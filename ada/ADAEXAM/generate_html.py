import os

files = ["1st.py", "2nd.py", "3rd.py", "4th.py", "5th.py", "6th.py", 
         "7th.py", "8th.py", "9th.py", "10th.py", "11th.py", "12th.py"]

titles = [
    "Linear Search",
    "Binary Search",
    "Tower of Hanoi",
    "Selection Sort",
    "Quick Sort",
    "Merge Sort",
    "Prim's Algorithm",
    "Floyd-Warshall Algorithm",
    "Tree Traversals",
    "Graph Coloring using Backtracking",
    "Job Sequencing with Deadlines",
    "0/1 Knapsack Problem"
]

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADA Exam Programs Reference</title>
    <style>
        * { box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background-color: #1e1e1e; /* VS Code dark background */
            color: #d4d4d4; /* Default VS Code text */
            margin: 0; 
            padding: 0; 
            display: flex;
            height: 100vh;
        }
        /* Sidebar container */
        .sidebar {
            width: 300px;
            background-color: #252526;
            border-right: 1px solid #3c3c3c;
            overflow-y: auto;
            position: fixed;
            height: 100vh;
        }
        .sidebar-header {
            padding: 10px 20px;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #858585;
        }
        .explorer-item {
            padding: 6px 20px;
            cursor: pointer;
            font-size: 13px;
            display: flex;
            align-items: center;
        }
        .explorer-item:hover {
            background-color: #2a2d2e;
            color: #ffffff;
        }
        .explorer-item b {
            margin-right: 8px;
            color: #519aba; /* Blue python icon mockup */
        }
        .explorer-item span {
            color: #9cdcfe;
            font-size: 11px;
            margin-left: 8px;
        }

        /* Main Editor area */
        .main-content {
            margin-left: 300px;
            flex-grow: 1;
            padding-bottom: 50px;
            overflow-y: auto;
        }
        
        .editor-container {
            margin: 40px auto;
            width: 90%;
            max-width: 1000px;
            background-color: #1e1e1e;
            border-radius: 5px;
            border: 1px solid #3c3c3c;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            overflow: hidden;
        }
        
        /* VS Code Top Tab */
        .tabs {
            display: flex;
            background-color: #252526;
            height: 35px;
            overflow: hidden;
            border-bottom: 1px solid #1e1e1e;
        }
        .tab-active {
            background-color: #1e1e1e;
            color: #ffffff;
            border-top: 2px solid #007acc;
            padding: 8px 15px;
            font-size: 13px;
            display: flex;
            align-items: center;
        }
        .breadcrumbs {
            padding: 5px 15px;
            font-size: 13px;
            color: #858585;
            border-bottom: 1px solid #2d2d2d;
            background-color: #1e1e1e;
        }
        .breadcrumbs span { color: #519aba; }

        /* Actual Code */
        pre { 
            margin: 0;
            padding: 20px; 
            overflow-x: auto; 
            font-family: 'Consolas', 'Courier New', Courier, monospace; 
            font-size: 14px; 
            line-height: 1.5; 
            background-color: #1e1e1e;
        }
        code { font-family: inherit; }
        
        /* VS Code Theme Syntax Colors */
        .keyword { color: #c586c0; }     /* return, yield, import, if, else, for, in */
        .keyword-blue { color: #569cd6; }/* def, class */
        .function { color: #dcdcaa; }    /* print, len, range, zip */
        .string { color: #ce9178; }      /* "text" */
        .number { color: #b5cea8; }      /* 0, 1, 999 */
        .comment { color: #6a9955; }     /* # comments */
        .operator { color: #d4d4d4; }    /* =, +, - */
    </style>
</head>
<body>

    <!-- SIDEBAR -->
    <div class="sidebar">
        <div class="sidebar-header">Explorer</div>
        <div class="sidebar-header" style="color: #cccccc;">ADA_EXAM_PREP</div>
        {sidebar}
    </div>

    <!-- MAIN EDITOR CONTENT -->
    <div class="main-content">
        {content}
    </div>

</body>
</html>
"""

sidebar_items = ""
content_blocks = ""

for f, title in zip(files, titles):
    path = os.path.join("/Users/harsh/Desktop/JavascriptPratice/ada/ADAEXAM", f)
    code = "File not found."
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            code = file.read().replace('<', '&lt;').replace('>', '&gt;')
            
            # Very basic syntax highlighting for better readability (VS Code Dark+ rules)
            # Strings basic (quick approximation that will work for most simple prints in these specific files)
            code = code.replace('"Enter elements:"', '<span class="string">"Enter elements:"</span>')
            code = code.replace('"Enter element to search:"', '<span class="string">"Enter element to search:"</span>')
            code = code.replace('"Enter the elements:"', '<span class="string">"Enter the elements:"</span>')
            code = code.replace('"Sorted:"', '<span class="string">"Sorted:"</span>')
            
            # Functions
            code = code.replace('print(', '<span class="function">print</span>(')
            code = code.replace('len(', '<span class="function">len</span>(')
            code = code.replace('range(', '<span class="function">range</span>(')
            code = code.replace('min(', '<span class="function">min</span>(')
            code = code.replace('max(', '<span class="function">max</span>(')
            code = code.replace('map(', '<span class="function">map</span>(')
            code = code.replace('split(', '<span class="function">split</span>(')
            code = code.replace('input(', '<span class="function">input</span>(')
            
            # Blue Keywords
            code = code.replace('def ', '<span class="keyword-blue">def</span> ')
            code = code.replace('class ', '<span class="keyword-blue">class</span> ')
            
            # Purple Keywords
            code = code.replace('if ', '<span class="keyword">if</span> ')
            code = code.replace('elif ', '<span class="keyword">elif</span> ')
            code = code.replace('else:', '<span class="keyword">else</span>:')
            code = code.replace('for ', '<span class="keyword">for</span> ')
            code = code.replace(' in ', ' <span class="keyword">in</span> ')
            code = code.replace('while ', '<span class="keyword">while</span> ')
            code = code.replace('return ', '<span class="keyword">return</span> ')
            code = code.replace('break', '<span class="keyword">break</span>')
    
    # Add to sidebar
    sidebar_items += f"""
        <div class="explorer-item">
            <b><small>Py</small></b> {f} <span>- {title.split(' ')[0]}</span>
        </div>
    """
    
    # Add to main content
    content_blocks += f"""
    <div class="editor-container">
        <div class="tabs">
            <div class="tab-active"><b><small style="color:#519aba;margin-right:6px">Py</small></b> {f}</div>
        </div>
        <div class="breadcrumbs">
            ADA_EXAM_PREP > <span>{f}</span> > {title}
        </div>
        <pre><code>{code}</code></pre>
    </div>
    """

full_html = html_template.replace("{sidebar}", sidebar_items).replace("{content}", content_blocks)

with open("/Users/harsh/Desktop/JavascriptPratice/ada/ADAEXAM/all_programs.html", "w", encoding="utf-8") as out:
    out.write(full_html)
print("Generated VS Code styled all_programs.html successfully!")
