#!/usr/bin/env Rscript

# Just to ram home the point that
# a client can be in any language, here's one
# in R.
#
# Reads from URLs like
# http://127.0.0.1:8000/database-summary?minTime=20251001000000&maxTime=20251031235959&site=L
# and writes daily summary charts to png files.
#
# The server from section 09 has to be running for this to work.
#
# To get the library, had to :
# sudo yum install curl-devel
# and then in R :
# install.packages("httr")
# install.packages("jsonlite")

# Import the http request library.
library(httr)
# Import the JSON parsing library.
library(jsonlite)

dir.create('daily')
# Loop through the sites.
siteCodes <- c('B', 'C', 'L', 'T', 'U')
baseURL='http://127.0.0.1:8000/database-summary?minTime=20251001000000&maxTime=20251031235959&site='

for (siteCode in siteCodes) {
  print(paste("Processing for site", siteCode))
  # Put together the url for the request for October
  # 2025 for this site.
  url <- paste(sep='', baseURL, siteCode)

  # Get the data.
  data <- httr::GET(url, accept_json())
  if (data$status_code != 200){
	cat("Something went wrong\n")
	q(save='no')
  }

  # Parse the JSON
  parsed_data <- content(data, "text", encoding = "UTF-8") |> fromJSON()

  # parsed_data looks like this :
  #    timerange   num
  # 1   20251001   503
  # 2   20251002   497
  # 3   20251003   489
  # 4   20251004   600

  print(paste(length(parsed_data$timerange), "points received"))


  # Do the bar plot.
  outFile <- paste(sep='', 'daily/october_2025_halpha_summary_', siteCode, '.png')
  print(paste("Writing to", outFile))
  png(outFile, height=800, width=1200)

  y_plot_max <- max(parsed_data$num)
  y_plot_range <- c(0, y_plot_max + 30) # Add 30 to make room for text on top of bar
  bp <- barplot(parsed_data$num, names.arg = substring(parsed_data$timerange,7),
        xlab = "Day of month",
        ylab = "Number of Observations", col = "steelblue",
        main = paste("October 2025 Data Summary for Site", siteCode),
        cex.main = 1.5, cex.lab = 1.2, cex.axis = 1.1, ylim=y_plot_range)
  # Add numbers on top of bars.
  text(
   x = bp,
   y = parsed_data$num + 1, labels = parsed_data$num, pos = 3, cex = 1.2, col = "black"
  )

}

q(save='no')

