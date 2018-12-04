library(tidyverse)
library(magrittr)
library(stringr)
rm(list=ls()) #-- zap all previous data elements

setwd('~/Classes/Data Analytics/project/')
if(!exists('Crimes')){
  Crimes <- read_rds('Crimes.rds')
}
Crimes %<>% mutate(District = case_when(is.na(District) ~ as.double(23),
                                        District == 31 ~ as.double(13), 
                                        T ~ as.double(District)))

a <- Crimes %>% group_by(Primary.Type) %>% summarise(n=n())
print(a)
a <- Crimes %>% group_by(Primary.Type, Description) %>% summarise(n=n())
print(a)


a <- Crimes %>% group_by(Year) %>% summarise(n=n())
print(a)

fig <- a %>% ggplot(aes(Year, n/1e+05)) +
  geom_line(stat = 'Identity', size = 1.5)+
  geom_point(stat = 'Identity', size = 3)+
  ylim(0,5)+
  xlab('Year')+ ylab('Number of Crimes (1.0e+5)')+
  theme_bw(base_size = 16)+
  theme(text = element_text(size = 16), panel.grid.major = element_line(colour = "gray"),
        legend.background = element_rect(color = 'black'))
print(fig)
ggsave('ByYear.png', fig, width = 6.66, height = 5, device = 'png')





a <- Crimes %>% group_by(Primary.Type) %>% summarise(n=n()) %>% 
  arrange(-n)
print(a)






