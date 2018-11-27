library(tidyverse)

#wikisent2 <- read_csv("~/_Fall_2018/CS450/ProjectWordly/Data/wikisent2.txt")

#words_reduced <- sample_n(wikisent2, size = 10000)

#words_reduced <- sample_n(words_reduced, size = 5000)

#write_csv(words_reduced, path = "~/_Fall_2018/CS450/ProjectWordly/Data/words_reduced.txt", col_names = FALSE, na = "")


words_reduced <- read_csv("~/_Fall_2018/CS450/ProjectWordly/Data/words_reduced.txt", col_names = FALSE)

words_reduced1 <- words_reduced %>%
  mutate(combined = str_c(X1, " ", X2, " ", X3)) %>%
  select(-c(X1, X2, X3)) %>%
  na.omit()

write_csv(words_reduced1, "Combined columns.csv", na = "")

words_reduced2 <- words_reduced1 %>%
  mutate(combined = tolower(combined),
         combined = str_replace_all(combined, ",", " "),
         combined = str_replace_all(combined, "'[[:punct:]]+", " "),
         combined = str_replace_all(combined, "\\)|\\(|\\.", " "))

write_csv(words_reduced2, "Combined - no punct.csv", na = "")

words_reduced3 <- words_reduced2 %>%
  separate(combined, into = c("1", "2", "3", "4", "5", "6",
                              "7", "8", "9", "10", "11", "12",
                              "13", "14", "15", "16", "17", "18",
                              "19", "20", "21", "22", "23", "24",
                              "25", "26", "27", "28", "29", "30",
                              "31", "32", "33", "34", "35", "36",
                              "37", "38", "39", "40", "41", "42",
                              "43", "44", "45", "46", "47", "48",
                              "49", "50", "51", "52", "53", "54"), sep = " ", extra = "drop")


write_csv(words_reduced3, path = "~/_Fall_2018/CS450/ProjectWordly/Data/words_separated.csv", na = "")







