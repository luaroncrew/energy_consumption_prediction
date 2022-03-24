library(shiny)

shinyUI(fluidPage(
  titlePanel("Prévision consommation énergie"),

  sidebarLayout(
    sidebarPanel(

      # Version 1 pour demander mois et année
      selectInput("Month", "Mois", c('Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Décembre')),
      selectInput("Year", "Année", seq(2015,2020)),

      # Version 2 pour demander mois et année
      dateInput('Month-Year',label = "Pédiode d'analyse : ",format = "mm/yyyy",language="fr",startview = "year"),

      sliderInput("Temp", "Température ", 10, min = -40, max = 50),

      verbatimTextOutput("value"),
      textOutput("resumeTemp"),
      textOutput("resumeConso"),
      tableOutput("tableau")
    ),
    mainPanel(
      plotOutput("nuage")
    )
  )
))