# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Addressing Overfitting

## Student Requirements

Before this lesson, you should be able to...

- Explain what overfitting is and how it arises.
- Train and evaluate scikit-learn models using train/test splits and cross-validation.

## Learning Objectives

After this lesson, you should be able use the following techniques to address overfitting:

- Incrementally adding or dropping features based on a heuristic such as correlation with the target
- Reducing the dimensionality of the feature space with PCA
- Shrinking coefficients with L1 and L2 regularization

## Lesson Module

[Addressing Overfitting](./modules/addressing_overfitting.ipynb)

## Next Steps

If you are struggling to address overfitting for your final project, try the techniques in this lesson. Otherwise, try these techniques on a different dataset e.g. from Kaggle where overfitting is a concern because the feature space is rich relative to the number of instances you have for training.

## Additional Resources

### Feature Selection

- [scikit-learn documentation](https://scikit-learn.org/stable/modules/feature_selection.html)

### Dimensionality Reduction

- [PCA Explained Visually](http://setosa.io/ev/principal-component-analysis/)
- [In Depth: Principal Component Analysis](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html)

### Regularization

- Ch. 6 from [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf)