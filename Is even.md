---


---

<h3 id="explanation-of-is_even-function">Explanation of <code>is_even</code> function</h3>
<p>This function checks whether the input number <code>n</code> is even. The solution takes into account both integer and floating-point inputs, as well as edge cases such as non-numeric values and floats with decimal parts. Here’s how the function works:</p>
<h4 id="code-walkthrough">Code Walkthrough:</h4>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">is_even</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">:</span> 
    <span class="token comment"># Check if the input 'n' is either an integer or a float</span>
    <span class="token comment"># If not, immediately return False since we only care about numbers</span>
    <span class="token comment"># Also ensures floats with a decimal part (like 3.5) are considered uneven</span>
    <span class="token keyword">if</span> <span class="token operator">not</span> <span class="token builtin">isinstance</span><span class="token punctuation">(</span>n<span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token builtin">int</span><span class="token punctuation">,</span> <span class="token builtin">float</span><span class="token punctuation">)</span><span class="token punctuation">)</span> <span class="token operator">or</span> n <span class="token operator">!=</span> <span class="token builtin">int</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">return</span> <span class="token boolean">False</span>  

    <span class="token comment"># check if n is divisible by 2. If divisible, it's even; otherwise, it's odd</span>
    <span class="token keyword">return</span> n <span class="token operator">%</span> <span class="token number">2</span> <span class="token operator">==</span> <span class="token number">0</span>

</code></pre>
<ol>
<li><strong>Input Type Check</strong>:
<ul>
<li>The first condition <code>isinstance(n, (int, float))</code> ensures that <code>n</code> is either an integer or a float. If <code>n</code> is of any other type (e.g., a string or list), the function immediately returns <code>False</code>.</li>
<li>The second part of the condition <code>n != int(n)</code> ensures that if <code>n</code> is a float, it doesn’t have a decimal part. If <code>n</code> has a decimal part, it is treated as uneven (for example, <code>3.5</code> will return <code>False</code>).</li>
</ul>
</li>
<li><strong>Even or Odd Check</strong>:
<ul>
<li>After confirming that <code>n</code> is either an integer or a whole number float, the function checks if <code>n % 2 == 0</code>. This checks if the number is divisible by 2, meaning it is even. If the number is even, it returns <code>True</code>; otherwise, it returns <code>False</code>.</li>
</ul>
</li>
</ol>
<h4 id="edge-cases-handled">Edge Cases Handled:</h4>
<ul>
<li><strong>Non-Numeric Input</strong>: If the input is not a number, such as a string or list, the function returns <code>False</code>.</li>
<li><strong>Floats with Decimal Parts</strong>: Floats like <code>3.5</code> or <code>-4.7</code> are considered uneven because they are not integers.</li>
<li><strong>Negative Numbers</strong>: The modulo operation works for negative numbers as well, so <code>-4 % 2 == 0</code> will return <code>True</code> (even number).</li>
<li><strong>Zero</strong>: <code>0 % 2 == 0</code> will return <code>True</code>, correctly identifying zero as an even number.</li>
</ul>
<h4 id="performance-considerations">Performance Considerations:</h4>
<ul>
<li><strong>Time Complexity</strong>: The time complexity of this solution is <code>O(1)</code>, which means the function runs in constant time, regardless of the size or value of <code>n</code>. The function checks the type of the input and performs a single modulo operation, both of which are constant-time operations.</li>
<li><strong>Space Complexity</strong>: The space complexity is also <code>O(1)</code> since no additional space is used beyond simple variables.</li>
</ul>
<h4 id="optimization">Optimization:</h4>
<ul>
<li>For this implementation :
<ul>
<li>The type check ensures that only valid numeric inputs are considered, avoiding unnecessary computations on unsupported types.</li>
<li>The check for floats with decimal parts ensures that only integers are considered for evenness, without introducing additional complexity.</li>
<li>The modulo operation (<code>n % 2</code>) is an efficient way to determine evenness and works for both positive and negative numbers.</li>
</ul>
</li>
</ul>
<p>In terms of optimization, the current solution is efficient and straightforward, offering constant time complexity <code>O(1)</code> for all operations.</p>
<hr>
<h3 id="conclusion">Conclusion:</h3>
<p>This function efficiently determines whether a given number <code>n</code> is even, handling various edge cases like non-numeric input and floats with decimals. The time complexity is constant (<code>O(1)</code>), making it optimal for this problem.</p>
<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

