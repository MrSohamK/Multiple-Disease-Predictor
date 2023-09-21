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
      "cell_type": "markdown",
      "metadata": {
        "id": "9B5Zl1UOBMAJ"
      },
      "source": [
        "Importing the Dependencies"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YOCpZ1Vm6cfW"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn import svm\n",
        "from sklearn.metrics import accuracy_score"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PZm-USrtB_q4"
      },
      "source": [
        "Data Collection & Analysis"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5YC2lGuVBiZA"
      },
      "source": [
        "\n",
        "parkinsons_data = pd.read_csv('/content/parkinsons.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "Iw8z6w60Djd2",
        "outputId": "ca177b83-79f9-46c5-89c0-42985b1923ba"
      },
      "source": [
        "\n",
        "parkinsons_data.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             name  MDVP:Fo(Hz)  MDVP:Fhi(Hz)  MDVP:Flo(Hz)  MDVP:Jitter(%)  \\\n",
              "0  phon_R01_S01_1      119.992       157.302        74.997         0.00784   \n",
              "1  phon_R01_S01_2      122.400       148.650       113.819         0.00968   \n",
              "2  phon_R01_S01_3      116.682       131.111       111.555         0.01050   \n",
              "3  phon_R01_S01_4      116.676       137.871       111.366         0.00997   \n",
              "4  phon_R01_S01_5      116.014       141.781       110.655         0.01284   \n",
              "\n",
              "   MDVP:Jitter(Abs)  MDVP:RAP  MDVP:PPQ  Jitter:DDP  MDVP:Shimmer  ...  \\\n",
              "0           0.00007   0.00370   0.00554     0.01109       0.04374  ...   \n",
              "1           0.00008   0.00465   0.00696     0.01394       0.06134  ...   \n",
              "2           0.00009   0.00544   0.00781     0.01633       0.05233  ...   \n",
              "3           0.00009   0.00502   0.00698     0.01505       0.05492  ...   \n",
              "4           0.00011   0.00655   0.00908     0.01966       0.06425  ...   \n",
              "\n",
              "   Shimmer:DDA      NHR     HNR  status      RPDE       DFA   spread1  \\\n",
              "0      0.06545  0.02211  21.033       1  0.414783  0.815285 -4.813031   \n",
              "1      0.09403  0.01929  19.085       1  0.458359  0.819521 -4.075192   \n",
              "2      0.08270  0.01309  20.651       1  0.429895  0.825288 -4.443179   \n",
              "3      0.08771  0.01353  20.644       1  0.434969  0.819235 -4.117501   \n",
              "4      0.10470  0.01767  19.649       1  0.417356  0.823484 -3.747787   \n",
              "\n",
              "    spread2        D2       PPE  \n",
              "0  0.266482  2.301442  0.284654  \n",
              "1  0.335590  2.486855  0.368674  \n",
              "2  0.311173  2.342259  0.332634  \n",
              "3  0.334147  2.405554  0.368975  \n",
              "4  0.234513  2.332180  0.410335  \n",
              "\n",
              "[5 rows x 24 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-09ab8692-d189-4aac-8b73-032a2a0c64be\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>name</th>\n",
              "      <th>MDVP:Fo(Hz)</th>\n",
              "      <th>MDVP:Fhi(Hz)</th>\n",
              "      <th>MDVP:Flo(Hz)</th>\n",
              "      <th>MDVP:Jitter(%)</th>\n",
              "      <th>MDVP:Jitter(Abs)</th>\n",
              "      <th>MDVP:RAP</th>\n",
              "      <th>MDVP:PPQ</th>\n",
              "      <th>Jitter:DDP</th>\n",
              "      <th>MDVP:Shimmer</th>\n",
              "      <th>...</th>\n",
              "      <th>Shimmer:DDA</th>\n",
              "      <th>NHR</th>\n",
              "      <th>HNR</th>\n",
              "      <th>status</th>\n",
              "      <th>RPDE</th>\n",
              "      <th>DFA</th>\n",
              "      <th>spread1</th>\n",
              "      <th>spread2</th>\n",
              "      <th>D2</th>\n",
              "      <th>PPE</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>phon_R01_S01_1</td>\n",
              "      <td>119.992</td>\n",
              "      <td>157.302</td>\n",
              "      <td>74.997</td>\n",
              "      <td>0.00784</td>\n",
              "      <td>0.00007</td>\n",
              "      <td>0.00370</td>\n",
              "      <td>0.00554</td>\n",
              "      <td>0.01109</td>\n",
              "      <td>0.04374</td>\n",
              "      <td>...</td>\n",
              "      <td>0.06545</td>\n",
              "      <td>0.02211</td>\n",
              "      <td>21.033</td>\n",
              "      <td>1</td>\n",
              "      <td>0.414783</td>\n",
              "      <td>0.815285</td>\n",
              "      <td>-4.813031</td>\n",
              "      <td>0.266482</td>\n",
              "      <td>2.301442</td>\n",
              "      <td>0.284654</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>phon_R01_S01_2</td>\n",
              "      <td>122.400</td>\n",
              "      <td>148.650</td>\n",
              "      <td>113.819</td>\n",
              "      <td>0.00968</td>\n",
              "      <td>0.00008</td>\n",
              "      <td>0.00465</td>\n",
              "      <td>0.00696</td>\n",
              "      <td>0.01394</td>\n",
              "      <td>0.06134</td>\n",
              "      <td>...</td>\n",
              "      <td>0.09403</td>\n",
              "      <td>0.01929</td>\n",
              "      <td>19.085</td>\n",
              "      <td>1</td>\n",
              "      <td>0.458359</td>\n",
              "      <td>0.819521</td>\n",
              "      <td>-4.075192</td>\n",
              "      <td>0.335590</td>\n",
              "      <td>2.486855</td>\n",
              "      <td>0.368674</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>phon_R01_S01_3</td>\n",
              "      <td>116.682</td>\n",
              "      <td>131.111</td>\n",
              "      <td>111.555</td>\n",
              "      <td>0.01050</td>\n",
              "      <td>0.00009</td>\n",
              "      <td>0.00544</td>\n",
              "      <td>0.00781</td>\n",
              "      <td>0.01633</td>\n",
              "      <td>0.05233</td>\n",
              "      <td>...</td>\n",
              "      <td>0.08270</td>\n",
              "      <td>0.01309</td>\n",
              "      <td>20.651</td>\n",
              "      <td>1</td>\n",
              "      <td>0.429895</td>\n",
              "      <td>0.825288</td>\n",
              "      <td>-4.443179</td>\n",
              "      <td>0.311173</td>\n",
              "      <td>2.342259</td>\n",
              "      <td>0.332634</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>phon_R01_S01_4</td>\n",
              "      <td>116.676</td>\n",
              "      <td>137.871</td>\n",
              "      <td>111.366</td>\n",
              "      <td>0.00997</td>\n",
              "      <td>0.00009</td>\n",
              "      <td>0.00502</td>\n",
              "      <td>0.00698</td>\n",
              "      <td>0.01505</td>\n",
              "      <td>0.05492</td>\n",
              "      <td>...</td>\n",
              "      <td>0.08771</td>\n",
              "      <td>0.01353</td>\n",
              "      <td>20.644</td>\n",
              "      <td>1</td>\n",
              "      <td>0.434969</td>\n",
              "      <td>0.819235</td>\n",
              "      <td>-4.117501</td>\n",
              "      <td>0.334147</td>\n",
              "      <td>2.405554</td>\n",
              "      <td>0.368975</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>phon_R01_S01_5</td>\n",
              "      <td>116.014</td>\n",
              "      <td>141.781</td>\n",
              "      <td>110.655</td>\n",
              "      <td>0.01284</td>\n",
              "      <td>0.00011</td>\n",
              "      <td>0.00655</td>\n",
              "      <td>0.00908</td>\n",
              "      <td>0.01966</td>\n",
              "      <td>0.06425</td>\n",
              "      <td>...</td>\n",
              "      <td>0.10470</td>\n",
              "      <td>0.01767</td>\n",
              "      <td>19.649</td>\n",
              "      <td>1</td>\n",
              "      <td>0.417356</td>\n",
              "      <td>0.823484</td>\n",
              "      <td>-3.747787</td>\n",
              "      <td>0.234513</td>\n",
              "      <td>2.332180</td>\n",
              "      <td>0.410335</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 24 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-09ab8692-d189-4aac-8b73-032a2a0c64be')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-09ab8692-d189-4aac-8b73-032a2a0c64be button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-09ab8692-d189-4aac-8b73-032a2a0c64be');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cK7L_o2TDuZb",
        "outputId": "ff4ba57f-ef7c-42e3-e76d-c6cd69e8b250"
      },
      "source": [
        "\n",
        "parkinsons_data.shape"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(195, 24)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NLmzHIgnEGi4",
        "outputId": "59986869-f8e1-47a7-cd80-aa699514e488"
      },
      "source": [
        "\n",
        "parkinsons_data.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 195 entries, 0 to 194\n",
            "Data columns (total 24 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   name              195 non-null    object \n",
            " 1   MDVP:Fo(Hz)       195 non-null    float64\n",
            " 2   MDVP:Fhi(Hz)      195 non-null    float64\n",
            " 3   MDVP:Flo(Hz)      195 non-null    float64\n",
            " 4   MDVP:Jitter(%)    195 non-null    float64\n",
            " 5   MDVP:Jitter(Abs)  195 non-null    float64\n",
            " 6   MDVP:RAP          195 non-null    float64\n",
            " 7   MDVP:PPQ          195 non-null    float64\n",
            " 8   Jitter:DDP        195 non-null    float64\n",
            " 9   MDVP:Shimmer      195 non-null    float64\n",
            " 10  MDVP:Shimmer(dB)  195 non-null    float64\n",
            " 11  Shimmer:APQ3      195 non-null    float64\n",
            " 12  Shimmer:APQ5      195 non-null    float64\n",
            " 13  MDVP:APQ          195 non-null    float64\n",
            " 14  Shimmer:DDA       195 non-null    float64\n",
            " 15  NHR               195 non-null    float64\n",
            " 16  HNR               195 non-null    float64\n",
            " 17  status            195 non-null    int64  \n",
            " 18  RPDE              195 non-null    float64\n",
            " 19  DFA               195 non-null    float64\n",
            " 20  spread1           195 non-null    float64\n",
            " 21  spread2           195 non-null    float64\n",
            " 22  D2                195 non-null    float64\n",
            " 23  PPE               195 non-null    float64\n",
            "dtypes: float64(22), int64(1), object(1)\n",
            "memory usage: 36.7+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "70rgu_k4ET9F",
        "outputId": "9d86783c-8f01-468a-a9a0-04552ebc10c7"
      },
      "source": [
        "\n",
        "parkinsons_data.isnull().sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "name                0\n",
              "MDVP:Fo(Hz)         0\n",
              "MDVP:Fhi(Hz)        0\n",
              "MDVP:Flo(Hz)        0\n",
              "MDVP:Jitter(%)      0\n",
              "MDVP:Jitter(Abs)    0\n",
              "MDVP:RAP            0\n",
              "MDVP:PPQ            0\n",
              "Jitter:DDP          0\n",
              "MDVP:Shimmer        0\n",
              "MDVP:Shimmer(dB)    0\n",
              "Shimmer:APQ3        0\n",
              "Shimmer:APQ5        0\n",
              "MDVP:APQ            0\n",
              "Shimmer:DDA         0\n",
              "NHR                 0\n",
              "HNR                 0\n",
              "status              0\n",
              "RPDE                0\n",
              "DFA                 0\n",
              "spread1             0\n",
              "spread2             0\n",
              "D2                  0\n",
              "PPE                 0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        },
        "id": "1AxFu0-nEhSA",
        "outputId": "333d5e58-f085-43dc-ccb1-e7fc75084bcf"
      },
      "source": [
        "# getting some statistical measures about the data\n",
        "parkinsons_data.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       MDVP:Fo(Hz)  MDVP:Fhi(Hz)  MDVP:Flo(Hz)  MDVP:Jitter(%)  \\\n",
              "count   195.000000    195.000000    195.000000      195.000000   \n",
              "mean    154.228641    197.104918    116.324631        0.006220   \n",
              "std      41.390065     91.491548     43.521413        0.004848   \n",
              "min      88.333000    102.145000     65.476000        0.001680   \n",
              "25%     117.572000    134.862500     84.291000        0.003460   \n",
              "50%     148.790000    175.829000    104.315000        0.004940   \n",
              "75%     182.769000    224.205500    140.018500        0.007365   \n",
              "max     260.105000    592.030000    239.170000        0.033160   \n",
              "\n",
              "       MDVP:Jitter(Abs)    MDVP:RAP    MDVP:PPQ  Jitter:DDP  MDVP:Shimmer  \\\n",
              "count        195.000000  195.000000  195.000000  195.000000    195.000000   \n",
              "mean           0.000044    0.003306    0.003446    0.009920      0.029709   \n",
              "std            0.000035    0.002968    0.002759    0.008903      0.018857   \n",
              "min            0.000007    0.000680    0.000920    0.002040      0.009540   \n",
              "25%            0.000020    0.001660    0.001860    0.004985      0.016505   \n",
              "50%            0.000030    0.002500    0.002690    0.007490      0.022970   \n",
              "75%            0.000060    0.003835    0.003955    0.011505      0.037885   \n",
              "max            0.000260    0.021440    0.019580    0.064330      0.119080   \n",
              "\n",
              "       MDVP:Shimmer(dB)  ...  Shimmer:DDA         NHR         HNR      status  \\\n",
              "count        195.000000  ...   195.000000  195.000000  195.000000  195.000000   \n",
              "mean           0.282251  ...     0.046993    0.024847   21.885974    0.753846   \n",
              "std            0.194877  ...     0.030459    0.040418    4.425764    0.431878   \n",
              "min            0.085000  ...     0.013640    0.000650    8.441000    0.000000   \n",
              "25%            0.148500  ...     0.024735    0.005925   19.198000    1.000000   \n",
              "50%            0.221000  ...     0.038360    0.011660   22.085000    1.000000   \n",
              "75%            0.350000  ...     0.060795    0.025640   25.075500    1.000000   \n",
              "max            1.302000  ...     0.169420    0.314820   33.047000    1.000000   \n",
              "\n",
              "             RPDE         DFA     spread1     spread2          D2         PPE  \n",
              "count  195.000000  195.000000  195.000000  195.000000  195.000000  195.000000  \n",
              "mean     0.498536    0.718099   -5.684397    0.226510    2.381826    0.206552  \n",
              "std      0.103942    0.055336    1.090208    0.083406    0.382799    0.090119  \n",
              "min      0.256570    0.574282   -7.964984    0.006274    1.423287    0.044539  \n",
              "25%      0.421306    0.674758   -6.450096    0.174351    2.099125    0.137451  \n",
              "50%      0.495954    0.722254   -5.720868    0.218885    2.361532    0.194052  \n",
              "75%      0.587562    0.761881   -5.046192    0.279234    2.636456    0.252980  \n",
              "max      0.685151    0.825288   -2.434031    0.450493    3.671155    0.527367  \n",
              "\n",
              "[8 rows x 23 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b83bb5a5-5785-498f-b146-d62b868ce2a6\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MDVP:Fo(Hz)</th>\n",
              "      <th>MDVP:Fhi(Hz)</th>\n",
              "      <th>MDVP:Flo(Hz)</th>\n",
              "      <th>MDVP:Jitter(%)</th>\n",
              "      <th>MDVP:Jitter(Abs)</th>\n",
              "      <th>MDVP:RAP</th>\n",
              "      <th>MDVP:PPQ</th>\n",
              "      <th>Jitter:DDP</th>\n",
              "      <th>MDVP:Shimmer</th>\n",
              "      <th>MDVP:Shimmer(dB)</th>\n",
              "      <th>...</th>\n",
              "      <th>Shimmer:DDA</th>\n",
              "      <th>NHR</th>\n",
              "      <th>HNR</th>\n",
              "      <th>status</th>\n",
              "      <th>RPDE</th>\n",
              "      <th>DFA</th>\n",
              "      <th>spread1</th>\n",
              "      <th>spread2</th>\n",
              "      <th>D2</th>\n",
              "      <th>PPE</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>...</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "      <td>195.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>154.228641</td>\n",
              "      <td>197.104918</td>\n",
              "      <td>116.324631</td>\n",
              "      <td>0.006220</td>\n",
              "      <td>0.000044</td>\n",
              "      <td>0.003306</td>\n",
              "      <td>0.003446</td>\n",
              "      <td>0.009920</td>\n",
              "      <td>0.029709</td>\n",
              "      <td>0.282251</td>\n",
              "      <td>...</td>\n",
              "      <td>0.046993</td>\n",
              "      <td>0.024847</td>\n",
              "      <td>21.885974</td>\n",
              "      <td>0.753846</td>\n",
              "      <td>0.498536</td>\n",
              "      <td>0.718099</td>\n",
              "      <td>-5.684397</td>\n",
              "      <td>0.226510</td>\n",
              "      <td>2.381826</td>\n",
              "      <td>0.206552</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>41.390065</td>\n",
              "      <td>91.491548</td>\n",
              "      <td>43.521413</td>\n",
              "      <td>0.004848</td>\n",
              "      <td>0.000035</td>\n",
              "      <td>0.002968</td>\n",
              "      <td>0.002759</td>\n",
              "      <td>0.008903</td>\n",
              "      <td>0.018857</td>\n",
              "      <td>0.194877</td>\n",
              "      <td>...</td>\n",
              "      <td>0.030459</td>\n",
              "      <td>0.040418</td>\n",
              "      <td>4.425764</td>\n",
              "      <td>0.431878</td>\n",
              "      <td>0.103942</td>\n",
              "      <td>0.055336</td>\n",
              "      <td>1.090208</td>\n",
              "      <td>0.083406</td>\n",
              "      <td>0.382799</td>\n",
              "      <td>0.090119</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>88.333000</td>\n",
              "      <td>102.145000</td>\n",
              "      <td>65.476000</td>\n",
              "      <td>0.001680</td>\n",
              "      <td>0.000007</td>\n",
              "      <td>0.000680</td>\n",
              "      <td>0.000920</td>\n",
              "      <td>0.002040</td>\n",
              "      <td>0.009540</td>\n",
              "      <td>0.085000</td>\n",
              "      <td>...</td>\n",
              "      <td>0.013640</td>\n",
              "      <td>0.000650</td>\n",
              "      <td>8.441000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.256570</td>\n",
              "      <td>0.574282</td>\n",
              "      <td>-7.964984</td>\n",
              "      <td>0.006274</td>\n",
              "      <td>1.423287</td>\n",
              "      <td>0.044539</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>117.572000</td>\n",
              "      <td>134.862500</td>\n",
              "      <td>84.291000</td>\n",
              "      <td>0.003460</td>\n",
              "      <td>0.000020</td>\n",
              "      <td>0.001660</td>\n",
              "      <td>0.001860</td>\n",
              "      <td>0.004985</td>\n",
              "      <td>0.016505</td>\n",
              "      <td>0.148500</td>\n",
              "      <td>...</td>\n",
              "      <td>0.024735</td>\n",
              "      <td>0.005925</td>\n",
              "      <td>19.198000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.421306</td>\n",
              "      <td>0.674758</td>\n",
              "      <td>-6.450096</td>\n",
              "      <td>0.174351</td>\n",
              "      <td>2.099125</td>\n",
              "      <td>0.137451</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>148.790000</td>\n",
              "      <td>175.829000</td>\n",
              "      <td>104.315000</td>\n",
              "      <td>0.004940</td>\n",
              "      <td>0.000030</td>\n",
              "      <td>0.002500</td>\n",
              "      <td>0.002690</td>\n",
              "      <td>0.007490</td>\n",
              "      <td>0.022970</td>\n",
              "      <td>0.221000</td>\n",
              "      <td>...</td>\n",
              "      <td>0.038360</td>\n",
              "      <td>0.011660</td>\n",
              "      <td>22.085000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.495954</td>\n",
              "      <td>0.722254</td>\n",
              "      <td>-5.720868</td>\n",
              "      <td>0.218885</td>\n",
              "      <td>2.361532</td>\n",
              "      <td>0.194052</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>182.769000</td>\n",
              "      <td>224.205500</td>\n",
              "      <td>140.018500</td>\n",
              "      <td>0.007365</td>\n",
              "      <td>0.000060</td>\n",
              "      <td>0.003835</td>\n",
              "      <td>0.003955</td>\n",
              "      <td>0.011505</td>\n",
              "      <td>0.037885</td>\n",
              "      <td>0.350000</td>\n",
              "      <td>...</td>\n",
              "      <td>0.060795</td>\n",
              "      <td>0.025640</td>\n",
              "      <td>25.075500</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.587562</td>\n",
              "      <td>0.761881</td>\n",
              "      <td>-5.046192</td>\n",
              "      <td>0.279234</td>\n",
              "      <td>2.636456</td>\n",
              "      <td>0.252980</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>260.105000</td>\n",
              "      <td>592.030000</td>\n",
              "      <td>239.170000</td>\n",
              "      <td>0.033160</td>\n",
              "      <td>0.000260</td>\n",
              "      <td>0.021440</td>\n",
              "      <td>0.019580</td>\n",
              "      <td>0.064330</td>\n",
              "      <td>0.119080</td>\n",
              "      <td>1.302000</td>\n",
              "      <td>...</td>\n",
              "      <td>0.169420</td>\n",
              "      <td>0.314820</td>\n",
              "      <td>33.047000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.685151</td>\n",
              "      <td>0.825288</td>\n",
              "      <td>-2.434031</td>\n",
              "      <td>0.450493</td>\n",
              "      <td>3.671155</td>\n",
              "      <td>0.527367</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>8 rows × 23 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b83bb5a5-5785-498f-b146-d62b868ce2a6')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b83bb5a5-5785-498f-b146-d62b868ce2a6 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b83bb5a5-5785-498f-b146-d62b868ce2a6');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3O8AclzwExyH",
        "outputId": "6a330028-c2a3-431a-f1cb-b529137cdcc7"
      },
      "source": [
        "\n",
        "parkinsons_data['status'].value_counts()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    147\n",
              "0     48\n",
              "Name: status, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L1srlxtEFYfN"
      },
      "source": [
        "1  --> Parkinson's Positive\n",
        "\n",
        "0 --> Healthy\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "id": "zUrPan7CFTMq",
        "outputId": "9addca6f-f25f-4cde-aa11-266fbece8b9f"
      },
      "source": [
        "\n",
        "parkinsons_data.groupby('status').mean()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        MDVP:Fo(Hz)  MDVP:Fhi(Hz)  MDVP:Flo(Hz)  MDVP:Jitter(%)  \\\n",
              "status                                                            \n",
              "0        181.937771    223.636750    145.207292        0.003866   \n",
              "1        145.180762    188.441463    106.893558        0.006989   \n",
              "\n",
              "        MDVP:Jitter(Abs)  MDVP:RAP  MDVP:PPQ  Jitter:DDP  MDVP:Shimmer  \\\n",
              "status                                                                   \n",
              "0               0.000023  0.001925  0.002056    0.005776      0.017615   \n",
              "1               0.000051  0.003757  0.003900    0.011273      0.033658   \n",
              "\n",
              "        MDVP:Shimmer(dB)  ...  MDVP:APQ  Shimmer:DDA       NHR        HNR  \\\n",
              "status                    ...                                               \n",
              "0               0.162958  ...  0.013305     0.028511  0.011483  24.678750   \n",
              "1               0.321204  ...  0.027600     0.053027  0.029211  20.974048   \n",
              "\n",
              "            RPDE       DFA   spread1   spread2        D2       PPE  \n",
              "status                                                              \n",
              "0       0.442552  0.695716 -6.759264  0.160292  2.154491  0.123017  \n",
              "1       0.516816  0.725408 -5.333420  0.248133  2.456058  0.233828  \n",
              "\n",
              "[2 rows x 22 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2223dde4-4970-4602-b034-347b3317c577\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MDVP:Fo(Hz)</th>\n",
              "      <th>MDVP:Fhi(Hz)</th>\n",
              "      <th>MDVP:Flo(Hz)</th>\n",
              "      <th>MDVP:Jitter(%)</th>\n",
              "      <th>MDVP:Jitter(Abs)</th>\n",
              "      <th>MDVP:RAP</th>\n",
              "      <th>MDVP:PPQ</th>\n",
              "      <th>Jitter:DDP</th>\n",
              "      <th>MDVP:Shimmer</th>\n",
              "      <th>MDVP:Shimmer(dB)</th>\n",
              "      <th>...</th>\n",
              "      <th>MDVP:APQ</th>\n",
              "      <th>Shimmer:DDA</th>\n",
              "      <th>NHR</th>\n",
              "      <th>HNR</th>\n",
              "      <th>RPDE</th>\n",
              "      <th>DFA</th>\n",
              "      <th>spread1</th>\n",
              "      <th>spread2</th>\n",
              "      <th>D2</th>\n",
              "      <th>PPE</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>status</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>181.937771</td>\n",
              "      <td>223.636750</td>\n",
              "      <td>145.207292</td>\n",
              "      <td>0.003866</td>\n",
              "      <td>0.000023</td>\n",
              "      <td>0.001925</td>\n",
              "      <td>0.002056</td>\n",
              "      <td>0.005776</td>\n",
              "      <td>0.017615</td>\n",
              "      <td>0.162958</td>\n",
              "      <td>...</td>\n",
              "      <td>0.013305</td>\n",
              "      <td>0.028511</td>\n",
              "      <td>0.011483</td>\n",
              "      <td>24.678750</td>\n",
              "      <td>0.442552</td>\n",
              "      <td>0.695716</td>\n",
              "      <td>-6.759264</td>\n",
              "      <td>0.160292</td>\n",
              "      <td>2.154491</td>\n",
              "      <td>0.123017</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>145.180762</td>\n",
              "      <td>188.441463</td>\n",
              "      <td>106.893558</td>\n",
              "      <td>0.006989</td>\n",
              "      <td>0.000051</td>\n",
              "      <td>0.003757</td>\n",
              "      <td>0.003900</td>\n",
              "      <td>0.011273</td>\n",
              "      <td>0.033658</td>\n",
              "      <td>0.321204</td>\n",
              "      <td>...</td>\n",
              "      <td>0.027600</td>\n",
              "      <td>0.053027</td>\n",
              "      <td>0.029211</td>\n",
              "      <td>20.974048</td>\n",
              "      <td>0.516816</td>\n",
              "      <td>0.725408</td>\n",
              "      <td>-5.333420</td>\n",
              "      <td>0.248133</td>\n",
              "      <td>2.456058</td>\n",
              "      <td>0.233828</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2 rows × 22 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2223dde4-4970-4602-b034-347b3317c577')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-2223dde4-4970-4602-b034-347b3317c577 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2223dde4-4970-4602-b034-347b3317c577');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8RY6c0waGSs7"
      },
      "source": [
        "Data Pre-Processing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "We7sRYu7Gc4q"
      },
      "source": [
        "Separating the features & Target"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UAcz8jFnFuzH"
      },
      "source": [
        "X = parkinsons_data.drop(columns=['name','status'], axis=1)\n",
        "Y = parkinsons_data['status']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "guRof_8WG1Yn",
        "outputId": "531b55ec-5615-47e6-dde6-51295bfe8945"
      },
      "source": [
        "print(X)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     MDVP:Fo(Hz)  MDVP:Fhi(Hz)  MDVP:Flo(Hz)  MDVP:Jitter(%)  \\\n",
            "0        119.992       157.302        74.997         0.00784   \n",
            "1        122.400       148.650       113.819         0.00968   \n",
            "2        116.682       131.111       111.555         0.01050   \n",
            "3        116.676       137.871       111.366         0.00997   \n",
            "4        116.014       141.781       110.655         0.01284   \n",
            "..           ...           ...           ...             ...   \n",
            "190      174.188       230.978        94.261         0.00459   \n",
            "191      209.516       253.017        89.488         0.00564   \n",
            "192      174.688       240.005        74.287         0.01360   \n",
            "193      198.764       396.961        74.904         0.00740   \n",
            "194      214.289       260.277        77.973         0.00567   \n",
            "\n",
            "     MDVP:Jitter(Abs)  MDVP:RAP  MDVP:PPQ  Jitter:DDP  MDVP:Shimmer  \\\n",
            "0             0.00007   0.00370   0.00554     0.01109       0.04374   \n",
            "1             0.00008   0.00465   0.00696     0.01394       0.06134   \n",
            "2             0.00009   0.00544   0.00781     0.01633       0.05233   \n",
            "3             0.00009   0.00502   0.00698     0.01505       0.05492   \n",
            "4             0.00011   0.00655   0.00908     0.01966       0.06425   \n",
            "..                ...       ...       ...         ...           ...   \n",
            "190           0.00003   0.00263   0.00259     0.00790       0.04087   \n",
            "191           0.00003   0.00331   0.00292     0.00994       0.02751   \n",
            "192           0.00008   0.00624   0.00564     0.01873       0.02308   \n",
            "193           0.00004   0.00370   0.00390     0.01109       0.02296   \n",
            "194           0.00003   0.00295   0.00317     0.00885       0.01884   \n",
            "\n",
            "     MDVP:Shimmer(dB)  ...  MDVP:APQ  Shimmer:DDA      NHR     HNR      RPDE  \\\n",
            "0               0.426  ...   0.02971      0.06545  0.02211  21.033  0.414783   \n",
            "1               0.626  ...   0.04368      0.09403  0.01929  19.085  0.458359   \n",
            "2               0.482  ...   0.03590      0.08270  0.01309  20.651  0.429895   \n",
            "3               0.517  ...   0.03772      0.08771  0.01353  20.644  0.434969   \n",
            "4               0.584  ...   0.04465      0.10470  0.01767  19.649  0.417356   \n",
            "..                ...  ...       ...          ...      ...     ...       ...   \n",
            "190             0.405  ...   0.02745      0.07008  0.02764  19.517  0.448439   \n",
            "191             0.263  ...   0.01879      0.04812  0.01810  19.147  0.431674   \n",
            "192             0.256  ...   0.01667      0.03804  0.10715  17.883  0.407567   \n",
            "193             0.241  ...   0.01588      0.03794  0.07223  19.020  0.451221   \n",
            "194             0.190  ...   0.01373      0.03078  0.04398  21.209  0.462803   \n",
            "\n",
            "          DFA   spread1   spread2        D2       PPE  \n",
            "0    0.815285 -4.813031  0.266482  2.301442  0.284654  \n",
            "1    0.819521 -4.075192  0.335590  2.486855  0.368674  \n",
            "2    0.825288 -4.443179  0.311173  2.342259  0.332634  \n",
            "3    0.819235 -4.117501  0.334147  2.405554  0.368975  \n",
            "4    0.823484 -3.747787  0.234513  2.332180  0.410335  \n",
            "..        ...       ...       ...       ...       ...  \n",
            "190  0.657899 -6.538586  0.121952  2.657476  0.133050  \n",
            "191  0.683244 -6.195325  0.129303  2.784312  0.168895  \n",
            "192  0.655683 -6.787197  0.158453  2.679772  0.131728  \n",
            "193  0.643956 -6.744577  0.207454  2.138608  0.123306  \n",
            "194  0.664357 -5.724056  0.190667  2.555477  0.148569  \n",
            "\n",
            "[195 rows x 22 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xSNrvkJoG3cY",
        "outputId": "db156ede-5d9e-4ab4-de6d-ead138a71faf"
      },
      "source": [
        "print(Y)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0      1\n",
            "1      1\n",
            "2      1\n",
            "3      1\n",
            "4      1\n",
            "      ..\n",
            "190    0\n",
            "191    0\n",
            "192    0\n",
            "193    0\n",
            "194    0\n",
            "Name: status, Length: 195, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WDeqEaaHHBAS"
      },
      "source": [
        "Splitting the data to training data & Test data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4c6nrCiVG6NB"
      },
      "source": [
        "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6OqUka96H35c",
        "outputId": "47eb1e86-5aa5-41f1-deb2-e02d9d2bffe7"
      },
      "source": [
        "print(X.shape, X_train.shape, X_test.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(195, 22) (156, 22) (39, 22)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QIOAtx35JUMg"
      },
      "source": [
        "Model Training"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fWlsaBNuJV5g"
      },
      "source": [
        "Support Vector Machine Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IDInA1u5JCZ9"
      },
      "source": [
        "model = svm.SVC(kernel='linear')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F01DNpqWKmaW",
        "outputId": "a681ba26-aa79-4b09-a0a3-ddd653726c52"
      },
      "source": [
        "\n",
        "model.fit(X_train, Y_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SVC(kernel='linear')"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1z_-nZfuLJrH"
      },
      "source": [
        "Model Evaluation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Rj3XAnF8LMF4"
      },
      "source": [
        "Accuracy Score"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5LwxNgnqK1Za"
      },
      "source": [
        "\n",
        "X_train_prediction = model.predict(X_train)\n",
        "training_data_accuracy = accuracy_score(Y_train, X_train_prediction)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-dS9tcGdLm41",
        "outputId": "bbc0b0cd-ed16-4430-f137-8fdaf1f2183d"
      },
      "source": [
        "print('Accuracy score of training data : ', training_data_accuracy)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy score of training data :  0.8717948717948718\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rNUO2uHmLtjY"
      },
      "source": [
        "\n",
        "X_test_prediction = model.predict(X_test)\n",
        "test_data_accuracy = accuracy_score(Y_test, X_test_prediction)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BsF3UnQ2L_aR",
        "outputId": "80347c36-1481-4ba3-9cf3-7ed635ca5a85"
      },
      "source": [
        "print('Accuracy score of test data : ', test_data_accuracy)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy score of test data :  0.8717948717948718\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QlR4JG4YMfOR"
      },
      "source": [
        "Building a Predictive System"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w0FjSoO1MGBU",
        "outputId": "a4715754-198f-4927-9df3-e8a104a9b154"
      },
      "source": [
        "input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)\n",
        "\n",
        "\n",
        "input_data_as_numpy_array = np.asarray(input_data)\n",
        "\n",
        "\n",
        "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
        "\n",
        "prediction = model.predict(input_data_reshaped)\n",
        "print(prediction)\n",
        "\n",
        "\n",
        "if (prediction[0] == 0):\n",
        "  print(\"The Person does not have Parkinsons Disease\")\n",
        "\n",
        "else:\n",
        "  print(\"The Person has Parkinsons\")\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n",
            "The Person does not have Parkinsons Disease\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/base.py:451: UserWarning: X does not have valid feature names, but SVC was fitted with feature names\n",
            "  \"X does not have valid feature names, but\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FCHCMHpshHU4"
      },
      "source": [
        "Saving the trained model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cdmTOR4MhHCB"
      },
      "source": [
        "import pickle"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4gN09lokhKuZ"
      },
      "source": [
        "filename = 'parkinsons_model.sav'\n",
        "pickle.dump(model, open(filename, 'wb'))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IKW4D5CqhP5X"
      },
      "source": [
        "\n",
        "loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for column in X.columns:\n",
        "  print(column)"
      ],
      "metadata": {
        "id": "m8FO1U8hRVm_",
        "outputId": "079be68d-fb39-4544-9100-c6388b397091",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "MDVP:Fo(Hz)\n",
            "MDVP:Fhi(Hz)\n",
            "MDVP:Flo(Hz)\n",
            "MDVP:Jitter(%)\n",
            "MDVP:Jitter(Abs)\n",
            "MDVP:RAP\n",
            "MDVP:PPQ\n",
            "Jitter:DDP\n",
            "MDVP:Shimmer\n",
            "MDVP:Shimmer(dB)\n",
            "Shimmer:APQ3\n",
            "Shimmer:APQ5\n",
            "MDVP:APQ\n",
            "Shimmer:DDA\n",
            "NHR\n",
            "HNR\n",
            "RPDE\n",
            "DFA\n",
            "spread1\n",
            "spread2\n",
            "D2\n",
            "PPE\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JPyuHFeDRXZU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}