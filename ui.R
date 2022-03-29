library(shiny)
library(shinythemes)


shinyUI(fluidPage(
  # Definition du theme
  theme = shinytheme("superhero"),
  
  # Definition du Titre 
  titlePanel("SAE Regression"),
  
  titlePanel("Representation graphique d'une prevision"),
  
  sidebarLayout(
    sidebarPanel(
      # Creation d'un Input de l'utilisateur pour la variable unique
      sliderInput("Temp", "Temperature ", 10, min = -10, max = 40)
    ), 
    mainPanel(
      plotOutput("graph")
    )
    
  )))










