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
         sentence = tolower(sentence)) %>%
  na.omit()

write_csv(amazon, path = "Data/amazon.csv")


# IMDB Reviews

imdb <- read.csv("Data/imdb_labelled - v2.txt", header=FALSE)

imdb <- imdb %>%
  mutate(sentence = case_when(
    is.na(V2)  ~  as.character(V1),
    TRUE       ~  str_c(as.character(V1), " ", as.character(V2)))) %>%
  select(sentence)

imdb <- imdb %>%
  mutate(sentence = str_remove_all(sentence, "\\.|,|\\!|\\?")) %>%
  mutate(sentence = tolower(sentence)) %>%
  na.omit()

write_csv(imdb, path = "Data/imdb.csv")
    

# Yelp Reviews

yelp <- read_csv("Data/yelp_labelled - v2.txt", col_names = FALSE)

yelp <- yelp %>%
  mutate(sentence = case_when(
    is.na(X2)  ~  X1,
    TRUE       ~  str_c(X1, " ", X2))) %>%
  select(sentence)

yelp <- yelp %>%
  mutate(sentence = str_remove_all(sentence, "\\.|,|\\!|\\?|(|)")) %>%
  mutate(sentence = tolower(sentence)) %>%
  na.omit()

write_csv(yelp, path = "Data/yelp.csv", na = "")


##############################################################

# Combine files

##############################################################

review_data <- bind_rows(amazon, imdb, yelp)

review_data <- review_data %>%
  separate(sentence, into = c("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "11", "12", "13", "14", "15", "16", "17", "18",
                      "19", "20", "21", "22", "23", "24", "25", "26",
                      "27", "28", "29", "30", "31", "32", "33", "34",
                      "35", "36", "37", "38", "39", "40", "41", "42",
                      "43", "44", "45", "46", "47", "48", "49", "50"), sep = " ", extra = "drop")

write_csv(review_data, path = "Data/review_data_tidy.csv", na = "")
