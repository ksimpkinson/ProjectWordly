library(tidyverse)


##########################################

# Clean up raw text files

##########################################

# Amazon Reviews

amazon <- read_csv("Data/amazon_cells_labelled - v2.txt", col_names=FALSE)

amazon <- amazon %>%
  mutate(sentence = case_when(
    is.na(X2)  ~  X1,
    TRUE       ~  str_c(X1, " ", X2))) %>%
  select(-c(X1, X2))

amazon <- amazon %>%
  mutate(sentence = str_remove_all(sentence, "\\.|,|\\!|\\?"),
         sentence = tolower(sentence))

write_csv(amazon, path = "Data/amazon.csv")


# IMDB Reviews

imdb <- read_csv("Data/Raw Data/imdb_labelled - Copy.txt", col_names=FALSE)
imdb <- read.csv("Data/imdb_labelled - v2.txt", header=FALSE)

imdb <- imdb %>%
  mutate(sentence = case_when(
    is.na(X2)  ~  X1,
    TRUE       ~  str_c(X1, " ", X2))) %>%
  mutate(sentence = case_when(
    is.na(X3)  ~  sentence,
    TRUE  ~  str_c(sentence, " ", X3))) %>%
  mutate(sentence = case_when(
    is.na(X3)  ~  sentence,
    TRUE  ~  str_c(sentence, " ", X3))) %>%
  mutate(sentence = case_when(
    is.na(X4)  ~  sentence,
    TRUE       ~  str_c(sentence, " ", X4))) %>%
  mutate(sentence = case_when(
    is.na(X5)  ~  sentence,
    TRUE       ~  str_c(sentence, " ", X5))) %>%
  mutate(sentence = case_when(
    is.na(X6)  ~  sentence,
    TRUE       ~  str_c(sentence, " ", X6))) %>%
  select(-c(X1, X2, X3, X4, X5, X6))

imdb <- imdb %>%
  mutate(sentence = str_remove_all(sentence, "\\.|,|\\!|\\?"))

write_csv(imdb, path = "Data/imdb.csv")
    

# Yelp Reviews

yelp <- read.delim("yelp_labelled - v2.txt", header=FALSE)


##############################################################

# Combine files

##############################################################

review_data <- bind_rows(amazon, imdb, yelp)

review_data1 <- review_data %>%
  select(V1) %>%
  mutate(V1 = str_replace_all(V1, "\\.", " "))

review_data2 <- review_data1 %>%
  separate(V1, into = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "11", "12", "13", "14", "15", "16", "17", "18",
                      "19", "20", "21", "22", "23", "24", "25", "26",
                      "27", "28", "29", "30", "31", "32", "33", "34",
                      "35", "36", "37", "38", "39", "40", "41", "42",
                      "43", "44", "45", "46", "47", "48", "49", "50"), sep = " ", extra = "drop")
