remove(list=rm())


data = read.csv("track.csv")

is.na(data)


names <- names(data)
print(names)




table(data$race)
race.clean <- data[!data$race == "Free Form Text Only",]
race.clean.table <- table(race.clean$race)
print(race.clean.table)

table(data$accepted)



acceptance_ratio <- data[,c("race", "accepted")]
acceptance_ratio.clean <- acceptance_ratio[!acceptance_ratio$race == "Free Form Text Only",]
table(acceptance_ratio.clean)


# Determine the white acceptance ratio
white <- acceptance_ratio[acceptance_ratio$race == "White",]
white_acceptance_ratio <-sum(white$accepted)/length(white$accepted)

black <- acceptance_ratio[acceptance_ratio$race == "Black or African American",]
black_acceptance_ratio <-sum(black$accepted)/length(black$accepted)

native <- acceptance_ratio[acceptance_ratio$race == "American Indian or Alaska Native",]
native_acceptance_ratio <-sum(native$accepted)/length(native$accepted)

asian <- acceptance_ratio[acceptance_ratio$race == "Asian",]
asian_acceptance_ratio <-sum(asian$accepted)/length(asian$accepted)






