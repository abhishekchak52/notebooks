
function i=lcr_oscillator(t,theta,frequ,ampl,quality)
    i(1) = theta(2);
    i(2) = ampl*cos(frequ*t) - q(1)/quality - sin(theta(1);
endfunction


init = [1 0]'
t_0 = 0;
t_list = 0:0.001:10;
omega_list=-5:0.01:5;
for i=1:length(omega_list)
    q = ode(init,t_0,t_list,list(lcr_oscillator,omega_list(i)))
    peak_current(i) = max(q(2,:))-min(q(2,:))
    disp(max(q(2,:))-min(q(2,:)));
end
//plot(t_list)
//y = sin(t_list).*feval(t_list,list(thick_spikes,0.1,1))
plot(omega_list,peak_current)

//y=feval(t_list,list(func,50))
//plot(y,'.')
//plot(fft(q))
//disp(func(0.1,100))
