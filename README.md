
This is a library for analysing information on different chemical reactions and outputting some chemical reaction rates on request.

## REQUIREMENTS

- Python 3.9.12

NOTE: I have tested this programming.py file in Python 3.9.12. My recommended version is Python 3.9.12.

<p align="right">(<a href="#top">back to top</a>)</p>

## USAGE

There are some functions, you can use them as shown below:

1. To enable to output all reaction rates at specified times:

```python
reactions = output_all_reactions(0.4) # For example: time = 0.4.
print(reactions)
```

2. To enable to output the five largest reaction rates at specified times:

```python
lrr = find_the_nlargest(0.4, 5) # For example: time = 0.4, number = 5.
print(lrr)
```

3. To enable to output the rate for a specific reaction at specified times:

```python
specific_reaction_rate(0.2, 'e- + H2 > e- + e- + H2+') # For example: time = 0.2, specific reaction = 'e- + H2 > e- + e- + H2+'.
```

4. To enable to output all rates for reactions having a specified product or reactant at specified times:

```python
spr = specified_product_or_reactant(0.3, 'p', 'Nh3') # For example: time = 0.3, type = 'p', product = 'Nh3'
print(spr)
```

5. To enable to output the (up to) 5 largest reaction rates for reactions having a specified product or reactants at specified times:

```python
result = specified_nlargest_reaction_rates(0.3,'p','nh3', 5) # For example: time = 0.3, type = 'p', product = 'nh3', number = 5.
```

6. To enable to output all rates for reactions producing/consuming a specified species at specified times:

```python
result_list = rates_for_producing_or_consuming(0.0, 'p', 'h') # For example: time = 0.0, type = 'p', producing = 'h'.
print(result_list)
```

7. To enable to output the (up to) 5 largest rates for reactions producing/consuming a specified species  at specified times:

```python
nlargest_rates_for_producing_or_consuming(0.1, 'c', 'e-', 5) # For example: time = 0.1, type = 'c', consuming = 'e-', number = 5.
```

8. (1) To enable to plot the graphs for Task 2 and 3:

Run the Task 2 and 3 above.

(2) To enable to plot the graphs for Task 4 and 5:

```python
plot_figures_sp(0.0, 'r', 'nh3', 5) For example: time = 0.0, type = 'r', reactant = 'nh3', number = 5.
```

(3) To enable to plot the graphs for Task 6 and 7:

```python
plot_figures_sp_poc(0.3, 'c', 'nh3', 5) For example: time = 0.3, type = 'c', consuming = 'nh3', number = 5.
```

## ISSUES

Please report issues via [GitHub Issues](https://github.com/UCL-MPHY0021-21-22/tracknaliser-Working-Group-3/issues).

<p align="right">(<a href="#top">back to top</a>)</p>

## CONTRIBUTING

Please refer to the project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

<p align="right">(<a href="#top">back to top</a>)</p>

## ACKNOWLEDGMENTS

The data in this project is confidential.


<p align="right">(<a href="#top">back to top</a>)</p>
