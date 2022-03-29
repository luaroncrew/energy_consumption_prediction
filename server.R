library(shiny)
library(readxl)

df = read_excel('models.xlsx')

pentes <- as.numeric(df$slope)
ordonnees <- as.numeric(df$intercept)
heures <- as.numeric(df$hour)

prevision <- function(heure,temperature) {
  temperature = temperature + 273.15
  pente = pentes[heure+1]
  ordonnee = ordonnees[heure+1]
  return(pente*temperature + ordonnee)
}


shinyServer(function(input, output) {
  output$graph <- renderPlot({plot(y = prevision(heures, input$Temp),x = heures,type = 'l')})
})
