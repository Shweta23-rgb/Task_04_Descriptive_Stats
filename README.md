# Task_04_Descriptive_Stats

##  How to Run the General Scripts

Before running, make sure you have Python (and the required packages) installed.  
If you’re using a virtual environment, **activate it first!**

---

### 1. **Pure Python Script**

python PurePython_Stats_GeneralScript.py

or

python3 PurePython_Stats_GeneralScript.py


### 2. **Pandas**

python Pandas_Stats_GeneralScript.py

### 3. **Polars**

python Polars_Stats_GeneralScript.py

**How it Works:**

Each script will prompt you to enter the path to your CSV file (for example: data.csv or a direct download URL).

The script will load your dataset, analyze it, and print a summary of statistics for both numeric and categorical columns directly in the terminal.

No need to modify the code; just follow the on-screen prompts.

Package Requirements
Pandas Script:
Requires pandas

Polars Script:
Requires polars

(Pure Python has no external dependencies.)

**You can install any missing libraries using:**

pip install pandas polars 

## 📊 Dataset & Script Descriptions

- **Facebook_Ads_Basic_Stats.ipynb**  
  Exploratory and summary statistics for the Facebook ads dataset using all three approaches (Pure Python, Pandas, Polars).

- **Facebook_Ads_GroupBy.ipynb**  
  Facebook ads dataset: groupby analysis (e.g., by page/account) using Python, Pandas, and Polars for deeper aggregation.

- **Facebook_Posts_Python_Pandas_Stats.ipynb**  
  Exploratory statistics and groupby analysis for the Facebook posts dataset using both Pandas and Pure Python.

- **Facebook_Posts_Polars_Stats.ipynb**  
  Both basic descriptive statistics and groupby analysis on Facebook posts using Polars, demonstrating end-to-end workflow in one notebook.

- **Twitter_Posts_Basic_Stats.ipynb**  
  Generates summary statistics for the Twitter posts dataset using all three libraries.

- **Twitter_Posts_GroupBy_Stats.ipynb**  
  Performs groupby analysis on the Twitter posts dataset (e.g., by account/source) to show deeper insights, using all three methods.

---

### ✅Data Cleaning & Results Validation

For each dataset, I handled missing or complex columns as needed, and **demonstrated that all three approaches (Pure Python, Pandas, and Polars) produce consistent, matching results** for both basic statistics and grouped aggregations.

- For **Facebook ads** and **Twitter posts**, analysis is split into two notebooks each:  
  1. One for basic (overall) statistics  
  2. One for groupby (aggregated) statistics.

- For **Facebook posts**, the Python+Pandas version combines basic and groupby in one, while the Polars version covers both workflows in a single notebook.

---

**General scripts** (with `_GeneralScript.py` in the name) allow you to run the same analysis on any CSV, demonstrating the flexibility of each approach.

You can also adapt the `Twitter_Posts_Basic_Stats.ipynb` as a notebook-based template for other datasets if you prefer working in Jupyter.

## Reflections on Approaches & Challenges

**Was it a challenge to produce identical results?**

Yes, it was sometimes challenging to get identical results across all three approaches (Pure Python, Pandas, and Polars).
The biggest challenge was handling complex columns—some columns had nested data (like lists or dictionaries) or missing values. Each tool deals with these differently, so I had to make sure I cleaned and unpacked these columns the same way before running any stats. Another challenge was making sure the way I grouped and aggregated the data matched exactly in each script, since function names and defaults can be slightly different.

**How did I overcome these challenges?**

To solve this, I:

Carefully checked data types and handled missing/complex values before running stats.

Used the same logic for calculating metrics (like means, groupbys, etc.) in all scripts, double-checking the output at every step.

Compared intermediate results often, not just the final output, to catch small mismatches early.

**Which approach was easier or more performant?**

Pandas is the easiest to use for most tasks—its syntax is very readable, and most descriptive stats can be done in one line.

Polars is very fast, especially with big datasets, and the syntax is similar to Pandas. But, some features are a bit new and the library can act differently with missing/complex data.

Pure Python (using just built-in functions and lists) is slow and very verbose. It’s good for understanding what’s happening “under the hood,” but I wouldn’t recommend it for real analysis.

If speed is important, Polars wins. If you want ease of use and lots of online help, Pandas is best.

**What would I recommend to a junior data analyst?*

I would recommend learning and starting with Pandas. It’s widely used, there are tons of tutorials and Stack Overflow answers, and it works great for most data analysis projects. Once you’re comfortable, try out Polars for faster analysis on larger datasets. Use Pure Python only if you want to practice the basics.

**Can ChatGPT or coding AI produce template code for each approach?**

Yes! ChatGPT and other coding AIs are very good at generating starter code for all three approaches.
If you ask for descriptive statistics on a dataset, these tools almost always give you a Pandas template by default (like df.describe()). For Polars, you usually have to specifically ask for it, since it’s newer.

**Do I agree with these default recommendations?**

Yes, I do! Pandas is the standard tool for a reason. It’s powerful, easy to learn, and has great community support. Polars is catching up fast, but Pandas is still the best starting point for new analysts. I agree with the AI’s “default” suggestion of Pandas, but it’s nice to see options for faster libraries (like Polars) or low-level practice (Pure Python).

**Summary:**

Producing the same results with all three tools took extra care, especially with data cleaning. Pandas is the easiest and most flexible for most people. Polars is fastest for big data, and Pure Python is mostly educational. Coding AIs give good template code (usually in Pandas), which matches what I’d recommend for beginners too.




