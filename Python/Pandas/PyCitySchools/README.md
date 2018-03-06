
- *Observed Trend 1*: Based on overall passing rates, all of the top five schools are charter schools, and all of the bottom five schools are district schools. Charter schools also outperform district schools in average math score, average reading score, percent passing math, and percent passing reading.
- *Observed Trend 2*: Which school a student attended appeared to have more of an impact on average math and reading scores than grade level. School size also appeared to influence average math and reading scores, as well as percent passing math and reading and overall passing rate, with students at small schools (less than 1,700 total students) faring better than those at medium or large schools.
- *Observed  Trend 3*: Per student budget was not a strong indicator of student performance (as measured by average math and reading scores, percent passing math and reading, and overall passing rate). Students at schools with per student budgets less than \$615 per student scored higher in each of these categories than those at schools with per student budgets above \$615 dollars per student.

**Conclusion**: School size and type appeared to be the best indicators for student performance based on these data.

**Future Questions**: How do charter schools compare in size to district schools? It is possible that students at charter schools perform better because those schools are smaller than district schools, but more analysis is needed before we can determine whether that is true.

# Getting Started: Importing Dependencies and Data


```python
# Dependencies
import pandas as pd
```


```python
# Importing raw data
csvpath1 = 'raw_data/schools_complete.csv'
csvpath2 = 'raw_data/students_complete.csv'

schools_df = pd.read_csv(csvpath1)
students_df = pd.read_csv(csvpath2)
```


```python
# Preview schools DataFrame
schools_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Preview students DataFrame
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>



# District Summary

Create a high level snapshot (in table form) of the district's key metrics, including:
- Total Schools
- Total Students
- Total Budget
- Average Math Score
- Average Reading Score
- % Passing Math
- % Passing Reading
- Overall Passing Rate (Average of the above two)


```python
# Calculating total schools, total students, total budget, avg. math score, and avg. reading score
total_schools = len(schools_df)
total_students = len(students_df)
total_budget = schools_df['budget'].sum()
avg_math = students_df['math_score'].mean()
avg_reading = students_df['reading_score'].mean()

#Creating dataframes with only students passing math and only students passing reading
passing_math = students_df[students_df['math_score'] >= 60]
passing_reading = students_df[students_df['reading_score'] >= 60]

# Calculating % passing in reading and math. Scores of 60 or above = passing
percent_passing_math = passing_math['math_score'].sum() / total_students
percent_passing_reading = passing_reading['reading_score'].sum() / total_students

# Adding a column for overall score (avg. of reading and math scores)
for student in students_df:
    students_df['overall_score'] = (students_df['reading_score'] + students_df['math_score']) / 2
    
# Creating a datframe with only passing students and calculating overall passing rate
passing_overall = students_df[students_df['overall_score'] >= 60]
percent_passing = passing_overall['overall_score'].sum() / total_students
```


```python
# Making table with total schools, total students, total budget, avg. math score,
# avg. reading score, % passing math, % passing reading, and % passing overall.
district_summary = pd.DataFrame({'Total Schools':total_schools,
                                 'Total Students':total_students,
                                 'Total Budget':total_budget,
                                 'Average Math Score':avg_math,
                                 'Average Reading Score':avg_reading,
                                 '% Passing Math':percent_passing_math,
                                 '% Passing Reading':percent_passing_reading,
                                 'Overall Passing Rate':percent_passing}, index=[0])

# Reordering columns to match preferred output format.
district_summary = district_summary[['Total Schools', 'Total Students','Total Budget', 'Average Math Score',
                  'Average Reading Score', '% Passing Math', '% Passing Reading', 'Overall Passing Rate']]

# Printing district summary
district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>74.678555</td>
      <td>81.87784</td>
      <td>80.342213</td>
    </tr>
  </tbody>
</table>
</div>



# School Summary

Create an overview table that summarizes key metrics about each school, including:
- School Name
- School Type
- Total Students
- Total School Budget
- Per School Budget
- Average Math Score
- Average Reading Score
- % Passing Math
- % Passing Reading
- Overall Passing Rate (Average of the above two)


```python
# Pulling subset of columns from schools_df to start school summary dataframe, then renaming columns.
school_summary = schools_df[['name', 'type', 'size', 'budget']]
school_summary = school_summary.rename(columns={'name':'School',
                                                'type':'School Type',
                                                'size':'Total Students',
                                                'budget':'Total School Budget'})

# Setting the index to the school name
school_summary.set_index(school_summary['School'], inplace=True)
#Dropping duplicate "School" column
school_summary = school_summary[['School Type', 'Total Students', 'Total School Budget']]

# Adding a column with per student budget
school_summary['Per Student Budget'] = school_summary['Total School Budget'] / school_summary['Total Students']

# Grouping students_df by school so we can summarize info from students_df for each school
grouped_students = students_df.groupby(['school'])

# Adding columns with average math and reading scores
school_summary['Average Math Score'] = grouped_students['math_score'].mean()
school_summary['Average Reading Score'] = grouped_students['reading_score'].mean()

# Grouping the dataframes with students passing math, reading, and overall by school so we can
# calculate % passing math, reading, and overall for each school
passing_math_grouped = passing_math.groupby('school')
passing_reading_grouped = passing_reading.groupby('school')
passing_overall_grouped = passing_overall.groupby('school')

# Adding columns for percent passing math, reading, and overall
school_summary['% Passing Math'] = passing_math_grouped['math_score'].sum() / school_summary['Total Students']
school_summary['% Passing Reading'] = passing_reading_grouped['reading_score'].sum() / school_summary['Total Students']
school_summary['Overall Passing Rate'] = passing_overall_grouped['overall_score'].sum() / school_summary['Total Students']

# Printing school summary
school_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>70.279054</td>
      <td>81.182722</td>
      <td>78.865444</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>70.120380</td>
      <td>81.158020</td>
      <td>78.814344</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>83.542589</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>71.068177</td>
      <td>80.934412</td>
      <td>78.945415</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>83.584128</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>83.631844</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>83.518837</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.079783</td>
      <td>81.033963</td>
      <td>78.874196</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>83.809133</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>83.942308</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>83.818611</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.310078</td>
      <td>80.744686</td>
      <td>78.689797</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>70.906112</td>
      <td>80.966394</td>
      <td>78.894665</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>70.999270</td>
      <td>80.746258</td>
      <td>78.773092</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>83.633639</td>
    </tr>
  </tbody>
</table>
</div>



# Top 5 Schools by Overall Passing Rate

Create a table highlighting the top 5 performing schools based on overall passing rate.


```python
# Sort school summary by passing rate (high to low), then save only top 5 rows.
school_summary.sort_values('Overall Passing Rate', ascending=False, inplace=True)
top_5_schools = school_summary.iloc[[0, 1, 2, 3, 4]]

# Printing top 5 schools by passing rate.
top_5_schools
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>83.942308</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>83.818611</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>83.809133</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>83.633639</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>83.631844</td>
    </tr>
  </tbody>
</table>
</div>



# Bottom 5 Schools by Overall Passing Rate

Create a table highlighting the bottom 5 performing schools based on overall passing rate.


```python
# Sort school summary by passing rate (low to high), then save only top 5 rows.
school_summary.sort_values('Overall Passing Rate', inplace=True)
bottom_5_schools = school_summary.iloc[[0, 1, 2, 3, 4]]

# Printing bottom 5 schools by passing rate.
bottom_5_schools
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>70.310078</td>
      <td>80.744686</td>
      <td>78.689797</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>70.999270</td>
      <td>80.746258</td>
      <td>78.773092</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>70.120380</td>
      <td>81.158020</td>
      <td>78.814344</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>70.279054</td>
      <td>81.182722</td>
      <td>78.865444</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>71.079783</td>
      <td>81.033963</td>
      <td>78.874196</td>
    </tr>
  </tbody>
</table>
</div>



# Math Scores by Grade

Create a table that lists the average math score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# To start, make separate groupby objects for each grade (grouped by school)
grade9 = students_df[students_df['grade']=='9th'].groupby('school')
grade10 = students_df[students_df['grade']=='10th'].groupby('school')
grade11 = students_df[students_df['grade']== '11th'].groupby('school')
grade12 = students_df[students_df['grade']=='12th'].groupby('school')

# Then calculate mean math scores and put into a dataframe
math_scores_by_grade = pd.DataFrame(grade9['math_score'].mean())
math_scores_by_grade.rename(columns={'math_score':'9th Grade'}, inplace=True)
math_scores_by_grade.index.rename('School', inplace=True)
math_scores_by_grade['10th Grade'] = grade10['math_score'].mean()
math_scores_by_grade['11th Grade'] = grade11['math_score'].mean()
math_scores_by_grade['12th Grade'] = grade12['math_score'].mean()

# Print math scores by grade for each school
math_scores_by_grade
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th Grade</th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>



# Reading Scores by Grade

Create a table that lists the average reading score for students of each grade level (9th, 10th, 11th, 12th) at each school.


```python
# Repeat the same process used for math scores by grade, but this time for reading.
reading_scores_by_grade = pd.DataFrame(grade9['reading_score'].mean())
reading_scores_by_grade.rename(columns={'reading_score':'9th Grade'}, inplace=True)
reading_scores_by_grade.index.rename('School', inplace=True)
reading_scores_by_grade['10th Grade'] = grade10['reading_score'].mean()
reading_scores_by_grade['11th Grade'] = grade11['reading_score'].mean()
reading_scores_by_grade['12th Grade'] = grade12['reading_score'].mean()

# Print math scores by grade for each school
reading_scores_by_grade
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th Grade</th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Spending

Create a table that breaks down school performances based on average Spending Ranges (Per Student).
Use 4 reasonable bins to group school spending. Include in the table each of the following:
- Average Math Score
- Average Reading Score
- % Passing Math
- % Passing Reading
- Overall Passing Rate (Average of the above two)


```python
# First get an idea of good bin sizes to use for the total budgets.
school_summary['Per Student Budget'].describe()
```




    count     15.000000
    mean     620.066667
    std       28.544368
    min      578.000000
    25%      591.500000
    50%      628.000000
    75%      641.500000
    max      655.000000
    Name: Per Student Budget, dtype: float64




```python
# Set names and boundaries for bins
bin_names = ['< $590', '$590-615', '$615-640', '> $640']
bins = [0, 590, 615, 640, school_summary['Per Student Budget'].max()]

# Now cut schools and place them into bins, then add bin category to schools dataframe
school_summary['Per Student Budget Category'] = pd.cut(school_summary['Per Student Budget'], bins, labels=bin_names)

# Merge budget category into students_df
students_df = pd.merge(students_df, school_summary[['Per Student Budget Category']],
                       how='left', left_on='school', right_index=True)
```


```python
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>overall_score</th>
      <th>Per Student Budget Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>72.5</td>
      <td>&gt; $640</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>77.5</td>
      <td>&gt; $640</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>75.0</td>
      <td>&gt; $640</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>62.5</td>
      <td>&gt; $640</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>90.5</td>
      <td>&gt; $640</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Grouping students_df by budget category so we can summarize info from students_df for each.
budget_grouped_students = students_df.groupby(['Per Student Budget Category'])

# Adding columns with average math and reading scores
school_summary_by_budget = pd.DataFrame(budget_grouped_students['math_score'].mean()).rename(columns={'math_score':
                                                                                                     'Average Math Score'})
school_summary_by_budget['Average Reading Score'] = budget_grouped_students['reading_score'].mean()

# Recreating dataframes for students passing math, reading, and overall
# so they now include budget category as well.
passing_math = students_df[students_df['math_score'] >= 60]
passing_reading = students_df[students_df['reading_score'] >= 60]
passing_overall = students_df[students_df['overall_score'] >= 60]

# Grouping the dataframes with students passing math, reading, and overall by budget category
# so we can calculate % passing math, reading, and overall for each.
passing_math_budget_grouped = passing_math.groupby('Per Student Budget Category')
passing_reading_budget_grouped = passing_reading.groupby('Per Student Budget Category')
passing_overall_budget_grouped = passing_overall.groupby('Per Student Budget Category')

# Adding columns for percent passing math, reading, and overall
school_summary_by_budget['% Passing Math'] = (passing_math_budget_grouped['math_score'].sum() / 
                                              budget_grouped_students['Student ID'].count())
school_summary_by_budget['% Passing Reading'] = (passing_reading_budget_grouped['reading_score'].sum() / 
                                                 budget_grouped_students['Student ID'].count())
school_summary_by_budget['% Overall Passing Rate'] = (passing_overall_budget_grouped['overall_score'].sum() / 
                                                      budget_grouped_students['Student ID'].count())

# Printing scores by budget category
school_summary_by_budget
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Per Student Budget Category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt; $590</th>
      <td>83.363065</td>
      <td>83.964039</td>
      <td>83.363065</td>
      <td>83.964039</td>
      <td>83.663552</td>
    </tr>
    <tr>
      <th>$590-615</th>
      <td>83.529196</td>
      <td>83.838414</td>
      <td>83.529196</td>
      <td>83.838414</td>
      <td>83.683805</td>
    </tr>
    <tr>
      <th>$615-640</th>
      <td>78.236441</td>
      <td>81.559460</td>
      <td>73.227990</td>
      <td>81.559460</td>
      <td>79.791342</td>
    </tr>
    <tr>
      <th>&gt; $640</th>
      <td>77.058995</td>
      <td>80.958411</td>
      <td>70.851448</td>
      <td>80.958411</td>
      <td>78.882507</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Size

Repeat the Per Student Budget breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).


```python
# First, get a good sense of what bins to use
school_summary['Total Students'].describe()
```




    count      15.000000
    mean     2611.333333
    std      1420.915282
    min       427.000000
    25%      1698.000000
    50%      2283.000000
    75%      3474.000000
    max      4976.000000
    Name: Total Students, dtype: float64




```python
# Set names and boundaries for bins
bin_names = ['Small (< 1,700)', 'Medium (1,700-3,400)', 'Large (> 3,400)']
bins = [0, 1700, 3400, school_summary['Total Students'].max()]

# Now cut schools and place them into bins, then add bin category to schools dataframe
school_summary['Size Category'] = pd.cut(school_summary['Total Students'], bins, labels=bin_names)

# Merge school size category into students_df
students_df = pd.merge(students_df, school_summary[['Size Category']],
                       how='left', left_on='school', right_index=True)
```


```python
# Grouping students_df by school size category so we can summarize info from students_df for each.
size_grouped_students = students_df.groupby(['Size Category'])

# Adding columns with average math and reading scores
school_summary_by_size = pd.DataFrame(size_grouped_students['math_score'].mean()).rename(columns={'math_score':
                                                                                                     'Average Math Score'})
school_summary_by_size['Average Reading Score'] = size_grouped_students['reading_score'].mean()

# Recreating dataframes for students passing math, reading, and overall
# so they now include school size category as well.
passing_math = students_df[students_df['math_score'] >= 60]
passing_reading = students_df[students_df['reading_score'] >= 60]
passing_overall = students_df[students_df['overall_score'] >= 60]

# Grouping the dataframes with students passing math, reading, and overall by size category
# so we can calculate % passing math, reading, and overall for each.
passing_math_size_grouped = passing_math.groupby('Size Category')
passing_reading_size_grouped = passing_reading.groupby('Size Category')
passing_overall_size_grouped = passing_overall.groupby('Size Category')

# Adding columns for percent passing math, reading, and overall
school_summary_by_size['% Passing Math'] = (passing_math_size_grouped['math_score'].sum() / 
                                              size_grouped_students['Student ID'].count())
school_summary_by_size['% Passing Reading'] = (passing_reading_size_grouped['reading_score'].sum() / 
                                                 size_grouped_students['Student ID'].count())
school_summary_by_size['% Overall Passing Rate'] = (passing_overall_size_grouped['overall_score'].sum() / 
                                                      size_grouped_students['Student ID'].count())

# Printing scores by school size category
school_summary_by_size
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Size Category</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt; 1,700)</th>
      <td>83.523375</td>
      <td>83.877115</td>
      <td>83.523375</td>
      <td>83.877115</td>
      <td>83.700245</td>
    </tr>
    <tr>
      <th>Medium (1,700-3,400)</th>
      <td>79.892255</td>
      <td>82.396762</td>
      <td>76.539155</td>
      <td>82.396762</td>
      <td>81.090023</td>
    </tr>
    <tr>
      <th>Large (&gt; 3,400)</th>
      <td>77.070764</td>
      <td>80.928365</td>
      <td>70.864297</td>
      <td>80.928365</td>
      <td>78.857329</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Type

Repeat the breakdown above for school size, but this time group schools based on school type (Charter vs. District).


```python
# Merge school type into students_df
students_df = pd.merge(students_df, school_summary[['School Type']],
                       how='left', left_on='school', right_index=True)
```


```python
# Grouping students_df by school type so we can summarize info from students_df for each.
school_type_grouped_students = students_df.groupby(['School Type'])

# Adding columns with average math and reading scores
school_summary_by_type = pd.DataFrame(school_type_grouped_students['math_score'].mean()).rename(columns={'math_score':
                                                                                                     'Average Math Score'})
school_summary_by_type['Average Reading Score'] = school_type_grouped_students['reading_score'].mean()

# Recreating dataframes for students passing math, reading, and overall
# so they now include school type as well.
passing_math = students_df[students_df['math_score'] >= 60]
passing_reading = students_df[students_df['reading_score'] >= 60]
passing_overall = students_df[students_df['overall_score'] >= 60]

# Grouping the dataframes with students passing math, reading, and overall by school type
# so we can calculate % passing math, reading, and overall for each.
passing_math_school_type = passing_math.groupby('School Type')
passing_reading_school_type = passing_reading.groupby('School Type')
passing_overall_school_type = passing_overall.groupby('School Type')

# Adding columns for percent passing math, reading, and overall
school_summary_by_type['% Passing Math'] = (passing_math_school_type['math_score'].sum() / 
                                              school_type_grouped_students['Student ID'].count())
school_summary_by_type['% Passing Reading'] = (passing_reading_school_type['reading_score'].sum() / 
                                                 school_type_grouped_students['Student ID'].count())
school_summary_by_type['Overall Passing Rate'] = (passing_overall_school_type['overall_score'].sum() / 
                                                      school_type_grouped_students['Student ID'].count())

# Printing scores by school size category
school_summary_by_type
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.406183</td>
      <td>83.902821</td>
      <td>83.406183</td>
      <td>83.902821</td>
      <td>83.654502</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.987026</td>
      <td>80.962485</td>
      <td>70.733393</td>
      <td>80.962485</td>
      <td>78.844955</td>
    </tr>
  </tbody>
</table>
</div>


