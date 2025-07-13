# Task_04_Descriptive_Stats

This project analyzes real election-related social media data from the **2024 U.S. Presidential Election** using three tools:

- ✅ Pure Python  
- ✅ Pandas  
- ✅ Polars  

I worked with **three datasets**:
- Facebook Ads  
- Facebook Posts  
- Twitter Posts  

For each dataset, I wrote **three separate Python scripts**, one for each tool, totaling **9 scripts**.  
The idea was to calculate basic descriptive statistics and generate visual insights — and also compare how each tool performs on the same task.

---

## 🛠 How to Run the Code

1. Make sure you have Python 3 installed.

2. Install the required libraries:

```bash
pip install pandas polars matplotlib seaborn
Place your dataset .csv files in the same folder as the scripts.

Run any script using:

bash
Copy
Edit
python3 script_name.py
Example:

bash
Copy
Edit
python3 pandas_fb_ads.py
Each script will:

Load the dataset

Clean the data

Print descriptive statistics

Show charts (like histograms, bar plots, etc.)

📊 What I Learned
Pure Python took the most effort — I had to manually implement things like mean, median, and plotting.

Pandas was the easiest and most intuitive. Everything just worked with built-in functions.

Polars was new for me, but super fast and great for larger datasets once I got used to its syntax.

🔍 Which Tool Will I Use Going Forward?
Pandas is my go-to — it’s powerful, user-friendly, and works smoothly with visualization libraries like Seaborn and Matplotlib.

Polars is excellent for performance — I’ll use it when working with very large files.

Pure Python was a good learning experience, but not something I’d use in real projects.

👶 What I’d Recommend to a Beginner
Start with Pandas. It’s easy, well-documented, and widely used.
Once comfortable, try Polars to speed things up.
Skip Pure Python unless you really want to learn how everything works behind the scenes.

🚧 Challenges I Faced
Getting identical outputs from all tools was tough due to differences in how they handle things like null values and data types.

Pure Python made it harder to group and plot data compared to Pandas and Polars.

I had to ensure missing values were handled the same way in all scripts for fair comparison.

📁 Datasets Not Included
The original dataset .csv files are not included in the GitHub repo because they are large and sensitive.
I’ve added them to .gitignore to avoid uploading them accidentally.

✅ Final Thoughts
This project helped me compare three different ways of doing descriptive stats.
It made me realize that the tool is less important than the logic — but having the right tool saves time and effort.

Thanks for checking out my work! 🌟





