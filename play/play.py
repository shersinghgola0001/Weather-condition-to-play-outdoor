{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wClGlHZtMjhm",
        "outputId": "8b14958a-85ac-42fc-8efc-fb570c2d351b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Likelihood Table for Outlook:\n",
            "Outlook   Play\n",
            "Overcast  Yes     0.444444\n",
            "Rainy     No      0.400000\n",
            "          Yes     0.333333\n",
            "Sunny     No      0.600000\n",
            "          Yes     0.222222\n",
            "dtype: float64\n",
            "\n",
            "Likelihood Table for Temperature:\n",
            "Temperature  Play\n",
            "Cool         No      0.200000\n",
            "             Yes     0.333333\n",
            "Hot          No      0.400000\n",
            "             Yes     0.222222\n",
            "Mild         No      0.400000\n",
            "             Yes     0.444444\n",
            "dtype: float64\n",
            "\n",
            "Likelihood Table for Humidity:\n",
            "Humidity  Play\n",
            "High      No      0.800000\n",
            "          Yes     0.333333\n",
            "Normal    No      0.200000\n",
            "          Yes     0.666667\n",
            "dtype: float64\n",
            "\n",
            "Likelihood Table for Windy:\n",
            "Windy  Play\n",
            "False  No      0.400000\n",
            "       Yes     0.666667\n",
            "True   No      0.600000\n",
            "       Yes     0.333333\n",
            "dtype: float64\n",
            "\n",
            "Posterior Probability:\n",
            "{'Yes': 0.8605851979345954, 'No': 0.1394148020654045}\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Sample weather dataset\n",
        "data = {\n",
        "    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],\n",
        "    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],\n",
        "    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],\n",
        "    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'True'],\n",
        "    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']\n",
        "}\n",
        "\n",
        "# Convert data into a DataFrame\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Function to calculate probabilities\n",
        "def calculate_probability(df, feature_col, target_col):\n",
        "    probabilities = df.groupby([feature_col, target_col]).size() / df.groupby(target_col).size()\n",
        "    return probabilities\n",
        "\n",
        "# Generate frequency tables for each feature and target variable\n",
        "outlook_prob = calculate_probability(df, 'Outlook', 'Play')\n",
        "temperature_prob = calculate_probability(df, 'Temperature', 'Play')\n",
        "humidity_prob = calculate_probability(df, 'Humidity', 'Play')\n",
        "windy_prob = calculate_probability(df, 'Windy', 'Play')\n",
        "\n",
        "# Print the likelihood tables\n",
        "print(\"Likelihood Table for Outlook:\")\n",
        "print(outlook_prob)\n",
        "print(\"\\nLikelihood Table for Temperature:\")\n",
        "print(temperature_prob)\n",
        "print(\"\\nLikelihood Table for Humidity:\")\n",
        "print(humidity_prob)\n",
        "print(\"\\nLikelihood Table for Windy:\")\n",
        "print(windy_prob)\n",
        "\n",
        "# Bayes Theorem to calculate posterior probability (example for a new data point)\n",
        "# For instance, if the Outlook is Sunny, Temperature is Cool, Humidity is Normal, and Windy is False\n",
        "posterior_prob = {\n",
        "    'Yes': outlook_prob['Sunny']['Yes'] * temperature_prob['Cool']['Yes'] * humidity_prob['Normal']['Yes'] * windy_prob['False']['Yes'] * (df['Play'].value_counts(normalize=True)['Yes']),\n",
        "    'No': outlook_prob['Sunny']['No'] * temperature_prob['Cool']['No'] * humidity_prob['Normal']['No'] * windy_prob['False']['No'] * (df['Play'].value_counts(normalize=True)['No'])\n",
        "}\n",
        "\n",
        "# Normalize probabilities\n",
        "total = sum(posterior_prob.values())\n",
        "posterior_prob = {key: value/total for key, value in posterior_prob.items()}\n",
        "\n",
        "# Print posterior probability\n",
        "print(\"\\nPosterior Probability:\")\n",
        "print(posterior_prob)\n"
      ]
    }
  ]
}
