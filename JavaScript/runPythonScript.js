/**
 *  JavaScript function to run python script
 */

function runPythonScript(path) {
    // Get the path to the Python script.
    var pythonScriptPath = path;
    // Run the Python script.
    subprocess.run(["python", pythonScriptPath]);
}