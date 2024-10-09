<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>EmojiLang 🧑‍💻🎨</h1>

<p><strong>EmojiLang</strong> is a fun and lightweight programming language that uses emojis to perform basic arithmetic operations. 
Instead of traditional mathematical operators, EmojiLang makes your code more expressive and enjoyable by using emojis like ➕, ➖, ✖️, 
and ➗ for addition, subtraction, multiplication, and division, respectively.</p>

<h2>What is EmojiLang?</h2>
<p>
EmojiLang is a unique and minimalist programming language designed to make arithmetic operations more fun by using emojis. 
It supports basic mathematical operations and has a simple syntax that allows users to perform calculations in a playful and expressive way.
</p>
<p>
This language was built using Python and demonstrates how to create a domain-specific language (DSL) with a custom lexer, parser, 
and interpreter. By leveraging Python’s flexibility, I implemented a fully functional emoji-based language interpreter.
</p>

<h2>How it Was Made</h2>
<p>EmojiLang was created using the following key components:</p>
<ul>
    <li><strong>Lexer</strong>: To tokenize the input expressions and identify emojis and numbers.</li>
    <li><strong>Parser</strong>: To parse the tokenized input and generate an abstract syntax tree (AST) for evaluation.</li>
    <li><strong>Interpreter</strong>: To traverse the AST and perform the arithmetic operations based on the emojis provided.</li>
</ul>
<p>The language is built in a modular way, and each part of the interpreter is split into logical files like <code>lexer.py</code>, 
<code>parser_ast.py</code>, and <code>interpreter.py</code>.</p>

<h2>Installation</h2>
<p>You can install EmojiLang from PyPI using <code>pip</code>:</p>

<pre><code>pip install emoji-lang</code></pre>

<h2>Usage</h2>
<p>Once installed, you can start using EmojiLang from your terminal. Simply run the command <code>emoji-lang</code> 
to enter the interactive shell and start typing emoji-based arithmetic expressions.</p>

<h3>Example:</h3>

<pre><code>$ emoji-lang
Enter your expression: ➕ 5 3
Result: 8

Enter your expression: ✖️ 7 4
Result: 28

Enter your expression: ➗ 9 3
Result: 3.0

Enter your expression: ➖ 10 2
Result: 8

Enter your expression: exit
</code></pre>

<p>The language supports basic arithmetic using the following emoji operators:</p>

<ul>
    <li><strong>➕</strong> : Addition</li>
    <li><strong>➖</strong> : Subtraction</li>
    <li><strong>✖️</strong> : Multiplication</li>
    <li><strong>➗</strong> : Division</li>
</ul>

<p>To exit the interactive shell, type <code>exit</code>.</p>

<h2>Features in Progress</h2>
<p>I'm actively working on adding new features to EmojiLang, including:</p>

<ul>
    <li><strong>Variables</strong>: The ability to declare and use variables. Example:</li>
</ul>

<pre><code>let 🍎 = 5
let 🍌 = 10
➕ 🍎 🍌  # Should output 15
</code></pre>

<ul>
    <li><strong>Conditionals</strong>: Support for conditional logic such as <code>if</code> statements. Example:</li>
</ul>

<pre><code>if ➕ 🍎 🍌 > 10:
    ➕ 5 3
else:
    ➖ 10 3
</code></pre>

<ul>
    <li><strong>Loops</strong>: Adding support for looping constructs such as <code>while</code> and <code>for</code>.</li>
    <li><strong>Enhanced Error Handling</strong>: Making error messages more user-friendly to help users understand syntax issues.</li>
    <li><strong>Extended Operations</strong>: Supporting more advanced operations like exponents, modulus, and maybe even emoji-based logical operators.</li>
</ul>

<h2>How to Contribute</h2>
<p>If you have ideas for new features, optimizations, or bug fixes, feel free to contribute!</p>
<ol>
    <li>Fork the repository: <a href="https://github.com/PranavKulkarni33/EmojiLang">EmojiLang on GitHub</a></li>
    <li>Create a new branch for your feature: <code>git checkout -b feature-name</code></li>
    <li>Commit your changes: <code>git commit -m 'Add some feature'</code></li>
    <li>Push to the branch: <code>git push origin feature-name</code></li>
    <li>Submit a pull request.</li>
</ol>

<h2>Developer</h2>
<p>Pranav Kulkarni.</p>

</body>
</html>
