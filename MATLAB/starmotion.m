%% *Движение звезд*

close all
clear variables
%% *Импорт данных*

spectra = importdata('spectra.csv')
lambdaStart = importdata('lambda_start.csv')
lambdaDelta = importdata('lambda_delta.csv')
starNames = importdata('star_names.csv')
%% *Константы*

lambdaPr = 656.28 %нм
speedOfLight = 299792.458 %км/с
%% Определение диапазона длин волн

count_obs = size(spectra, 1) %количество наблюдений
count_stars = size(starNames, 1) %количество звезд
lambdaEnd = lambdaStart + (count_obs - 1) * lambdaDelta
lambda = (lambdaStart : lambdaDelta: lambdaEnd)'
%% Расчет скоростей удаления для каждой из звезд и построение графика

speed = zeros(count_stars, 1) 

fg1 = figure

for i = 1:count_stars
    s = spectra(:, i)
    [sHa, idx] = min(s)
    lambdaHa = lambda(idx)    

    z = lambdaHa/lambdaPr - 1
    speed_star = z * speedOfLight    
    speed(i) = speed_star

    if speed(i) > 0
        plot(lambda, s, "LineWidth", 3)
    else
        plot(lambda, s, '--', "LineWidth", 1)
    end
    hold on    
end

set(fg1, 'Visible', 'on')
grid on
xlabel('Длина волны, нм')
ylabel(['Интенсивность, эрг/см^2/с/', char(197)])
title({'Спектры звезд'})
legend(starNames)
text(lambdaStart + 10, 3.25 * 10^-13,  'Зубаиров Данис Б04-007')
hold off 

saveas(fg1, 'spectra.png')
%% Создание вектора movaway 

movaway = starNames((speed)' > 0)