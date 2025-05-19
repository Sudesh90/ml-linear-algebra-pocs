# Create the matrix
A <- matrix(c(1, 2, 4,
              2, 4, 7,
              3, 6, 9), 
            nrow = 3, byrow = TRUE)

# Load the Matrix package (optional, for better rank function)
library(Matrix)
#library(pragmatic);

# Calculate the rank
rank_A <- rankMatrix(A)
print(rank_A)