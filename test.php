<!DOCTYPE html>
<html>
<head>
    <title>Execute Command and SQL Query</title>
    <style>
        #container {
            display: flex;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            max-width: 1200px;
            margin: 0 auto;
        }

        #result, #sql-result {
            flex: 1;
            margin-right: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            overflow: auto;
        }

        #history, #sql-history {
            width: 200px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            overflow: auto;
        }

        #current-dir {
            margin-bottom: 10px;
        }

        .module {
            display: flex;
            margin-right: 20px;
        }
    </style>
</head>
<body>
    
    <div id='container'>
        <div class="module">
            <div id='history'>
                <h3>Command History</h3>
                            </div>
            <form method='post'>
                <label for='code'>Enter a shell command:</label>
                <input type='text' name='code' id='code' value=''>
                <input type='submit' name='run' value='Run'>
            </form>
            <div id='result'>
                <h3>Shell Result</h3>
                            </div>
        </div>
    </div>
    <div id='container'>
        <div class="module">
            <div id='sql-history'>
                <h3>SQL History</h3>
                            </div>
            <form method='post'>
                <label for='sql'>Enter an SQL query:</label>
                <input type='text' name='sql' id='sql' value=''>
                <input type='submit' name='run-sql' value='Run'>
            </form>
            <div id='sql-result'>
                <h3>SQL Result</h3>
                            </div>
        </div>
    </div>

    <div id='current-dir'>
        <strong>Current Directory:</strong> /home/mskzreo/gamooks/pp    </div>
</body>
</html>
