# PageRank
PageRank algorithm, which is used to rank web pages based on their importance.

This code implements the **PageRank** algorithm, which is used to rank web pages based on their importance. It uses two methods: **sampling** and **iteration**. Here's a breakdown of the code and its functions:

### **Main Function (`main`)**:
- **Argument Handling**: The program expects a directory path containing HTML files as a command-line argument.
- **Crawl**: The `crawl` function is used to parse the HTML files in the directory, extracting links from each page.
- **PageRank Calculation**: 
  - **Sampling**: The `sample_pagerank` function computes the PageRank by randomly sampling pages and updating the rank based on transition probabilities.
  - **Iteration**: The `iterate_pagerank` function calculates the PageRank using the iterative method, updating page ranks until the values converge.

### **Crawl Function (`crawl`)**:
- **HTML Parsing**: Reads all HTML files in the specified directory and extracts the hyperlinks (`<a href="...">`) from each file.
- **Link Filtering**: Removes self-links (links pointing to the same page) and ensures that only valid links to other pages within the corpus are retained.
- **Returns**: A dictionary where keys are page names, and values are the set of pages they link to.

### **Transition Model (`transition_model`)**:
- **Calculating Transition Probabilities**: This function returns a probability distribution for transitioning from one page to another. It considers a **damping factor** (usually set to 0.85), which gives a random probability for each page and a probability based on the links from the current page.
  - If a page has links, the function distributes the transition probability based on the damping factor and the number of links on the current page.
  - If a page has no links, the transition is evenly distributed among all pages.

### **Sampling PageRank (`sample_pagerank`)**:
- **Random Sampling**: This function estimates PageRank values by randomly sampling pages, starting from a random page, and transitioning to other pages based on the transition model.
- **Normalization**: After collecting samples, the ranks are normalized to sum up to 1, giving a probability distribution of ranks.

### **Iterative PageRank (`iterate_pagerank`)**:
- **Iterative Calculation**: This function iteratively updates the rank of each page by considering all pages that link to it. The rank of a page is calculated as the sum of the ranks of pages linking to it, weighted by the size of the link set.
- **Convergence**: The process stops when the difference between the old and new ranks is smaller than a threshold (0.001 in this case), meaning the ranks have converged.

### **Constants**:
- **DAMPING**: The damping factor (usually set to 0.85) controls the likelihood that a user will continue clicking on links rather than jumping to a random page.
- **SAMPLES**: The number of random samples to take in the sampling approach.

### **How It Works**:
1. **Crawl the Corpus**: The `crawl` function parses the HTML files in a given directory to build a link structure of the corpus.
2. **Sample PageRank**: Using the `sample_pagerank` function, a random walk is performed on the corpus, and the ranks of pages are updated based on the number of visits to each page.
3. **Iterative PageRank**: The `iterate_pagerank` function computes the PageRank by iteratively updating the ranks until they converge.
4. **Print Results**: Finally, the results of both methods (sampling and iteration) are printed, showing the PageRank of each page.

### **Usage**:
To run this program, you need a directory containing HTML files that represent web pages. Run the script with the directory path as an argument, like so:
```bash
python pagerank.py corpus_directory
```

This will print the PageRank results calculated using both sampling and iteration methods.




NOTE: USE YOUR OWN CORPUS, DATA IS CONFIDENTIAL
