library(shiny)

# install.packages("ggplot2")
library(readxl)

df = read_excel('models.xlsx')

pentes <- as.numeric(df$slope)
ordonnees <- as.numeric(df$intercept)
heures <- as.numeric(df$hour)

prevision <- function(heure,temperature) {
  pente = pentes[heure+1]
  ordonnee = ordonnees[heure+1]
  return(pente*temperature + ordonnee)
}

# Création du graphique
shinyServer(function(input, output) {
  output$graph <- renderPlot({plot(y = prevision(heures, input$Temp),x = heures,type = 'l')})
})
