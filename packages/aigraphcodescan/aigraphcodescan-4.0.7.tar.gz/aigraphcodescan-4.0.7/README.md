# AIGraphCodeScan

**AIGraphCodeScan** is a tool designed for performing security reviews of codebases using graph analysis. The package utilizes Neo4j and Fast GraphRAG to query and visualize relationships within the code, helping identify potential security risks and vulnerabilities by analyzing the structure and flow of the code.

## Features

- **Graph-based Code Analysis**: Leverages graph theory to analyze code relationships and interactions.
- **Neo4j Integration**: Stores and queries code structure and data flow in a Neo4j graph database.
- **Security Review**: Helps identify potential security vulnerabilities based on the code's structure and relationships.

## Installation

### Prerequisites

Ensure you have Python 3.6 or higher installed. You will also need a Neo4j instance running to store and query code-related data.

### Installation Steps

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/tcosolutions/aigraphcodescan.git
cd aigraphcodescan
pip install -e .
```

### Requirements

- Python 3.6+
- `neo4j >= 4.0.0`
- `fast_graphrag >= 0.1.0`

## Usage

Once installed, you can use the `aigraphcodescan` command to run the security review.

```bash
aigraphcodescan --directory=/home/user/vulncode --grapdirectory=/home/user/aigraphcodescan/vulncode_graph --debug
```

Graphdirectory defaults to current directory where aigraphcodescan is run, but can be set to different location as needed.

Export env variable for OpenAI (api key) and Neo4j settings (see code)

bash
```
export OPENAI_API_KEY="sk-..."
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"
```

Neo4j's visualization software Neo4j Browser can be used to graphically look at the CPG nodes and edges.

Please make sure, that the APOC plugin is enabled on your neo4j server. It is used in mass-creating nodes and relationships.

For example using docker:
```
docker run -p 7474:7474 -p 7687:7687 -d -e NEO4J_AUTH=neo4j/password -e NEO4JLABS_PLUGINS='["apoc"]' neo4j:5
```

The command will start the graph-based security review process. The `--debug` option enables more detailed logging output.

## Example Workflow

1. **Run the security scan**: Use the `aigraphcodescan` command to analyze your codebase.
2. **Review findings**: Based on the graph analysis, the tool will provide insights into potential security vulnerabilities, such as unexpected interactions between modules, exposed endpoints, or insecure data flows.
3. **Improve your code**: Use the output to guide security improvements in your codebase.


Automated Setup and Scan for aigraphcodescan

This guide explains how to use the provided shell script to automate the installation of dependencies and the execution of the aigraphcodescan security review tool.
Prerequisites

    A compatible operating system (Ubuntu/Debian-based Linux or macOS).

    sudo access for Docker installation (on Linux).

    pip and python3 installed.

How the Script Works

The setup_and_run_aigraphcodescan.sh script performs the following actions:

    Argument Check: It verifies that you have provided a target directory to scan.

    Docker Check: It checks if Docker is installed. If not, it attempts to install it on Ubuntu/Debian Linux. On macOS, it will prompt you to install it manually.

    Neo4j Container: It checks for a running Neo4j container. If one is not found, it automatically starts a new one with the necessary APOC plugin and default credentials.

    aigraphcodescan Installation: It checks if the aigraphcodescan command is available. If not, it installs it from PyPI using pip.

    OpenAI API Key: It looks for an OPENAI_API_KEY in a file at ~/.openai_api_key. If the file doesn't exist, it will interactively prompt you for the key and save it securely.

    Environment Variables: It exports the required environment variables for Neo4j and the OpenAI API key.

    Scan Execution: It runs the aigraphcodescan command with the provided directory, a default graph directory, and the debug flag.

Usage

    Make the script executable:

    chmod +x setup_and_run_aigraphcodescan.sh

    Run the script:
    Execute the script, providing the path to the directory containing the code you want to scan.

    ./setup_and_run_aigraphcodescan.sh --directory /path/to/your/code

    Replace /path/to/your/code with the actual directory you wish to scan.

Notes

    Permissions: On Linux, you might need to run sudo usermod -aG docker $USER after the first-time Docker installation and then log out and log back in to run Docker commands without sudo.

    Neo4j Browser: Once the script starts the Neo4j container, you can access the Neo4j Browser for visualization at http://localhost:7474. Use the username neo4j and the password password to log in.

    Graph Directory: The graph data will be saved in a new directory named after your scanned directory, appended with _graph (e.g., /path/to/your/code_graph).

## The Difficulty of Building a CPG/DFG


Building these graphs involves much more than just traversing an Abstract Syntax Tree (AST):

* Parsing and Lexing: You first need a robust parser that can handle all the quirks and edge cases of the target programming language.
* Symbol Resolution: To create a DFG, your tool needs to know what every variable and function name refers to, even across different files or modules. This is a hard problem known as symbol resolution or name binding.
* Interprocedural Analysis: To be truly useful, the graphs must analyze the flow of data and control between different functions. This requires tracking data from a function's arguments to its return values and identifying which functions call which others. This is one of the most complex parts of static analysis.
* Handling of Aliases and Pointers: Languages like C have pointers and aliasing (when two variables refer to the same memory location), which make data flow analysis exceptionally difficult. You need sophisticated algorithms to correctly track which data is "tainted" and where it flows.
* Because of this complexity, most developers rely on existing, purpose-built static analysis tools and libraries like Joern, CodeQL, or Semgrep, which handle the heavy lifting of graph generation.

LLMs and Graph Generation
Yes, an LLM can create a simplified CPG or DFG from source code. However, there are significant caveats:
* Limited Scope: The LLM's graph will be based on its understanding of the code's syntax and its training data. It can likely produce a basic graph for a small, self-contained program. However, it will struggle with larger, more complex projects that involve multiple files, external libraries, and dynamic behaviors.
* Inaccuracy and Hallucination: LLMs can hallucinate or misinterpret code, leading to incorrect or incomplete graphs. They don't truly "execute" the code or have a formal model of its behavior.
** Security Concerns: ** For security-critical applications like SAST, the generated graph must be 100% accurate. A single missed data flow edge could hide a critical vulnerability. An LLM's output cannot be trusted for this purpose without extensive, manual verification.
  
In short, while an LLM can be used to assist in understanding code or generating small snippets for graph creation, it is not a reliable substitute for a dedicated static analysis engine. A developer or security analyst would use an LLM for prototyping or explanation, but would rely on a robust, validated tool for any serious analysis.

In case of this approach (LLM, graph rag) it will come to how well nodes and edges are identified, as well as sinks and tainting/sanitization.



## Contributing

We welcome contributions to **AIGraphCodeScan**. If you find a bug or have a suggestion, please open an issue or submit a pull request.

## License

This project is licensed under the AGPL 3.0 License - see the [LICENSE](LICENSE) file for details.
