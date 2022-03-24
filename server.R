library(shiny)

Jour = seq(31)
Conso = sample(x = 31)

shinyServer(function(input, output) {
  output$nuage <- renderPlot({
    plot(Jour,Conso, main = "Consommation")
  })

  output$resumeTemp <- renderText({
    paste("Moyenne Température :", mean(mtcars$mpg, na.rm = T))
  })
  output$resumeConso <- renderText({
    paste("Moyenne Consommation", input$choix, ":", mean(mtcars[,input$choix], na.rm = T))
  })
})