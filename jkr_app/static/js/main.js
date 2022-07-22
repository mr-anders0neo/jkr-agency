"use strict";

// Initialize functions
document.addEventListener('DOMContentLoaded', () => {
    // include charts in services page only
    document.querySelector('.jkr-services') ? chartFunction() : '';
    // initialize hamburger menu on mobile
    hamburgerMenu();
    // initialize login dialog box
    loginDialog();
    // handle redirect to services page
    redirectServices();
    // initialize the carousel
    initCarousel();
    // logout user
    logoutUser();
    // check user login
    loginUser();
});

// Chart.js function
const chartFunction = () => {
    // load line chart showing florida house prices
    const line = document.getElementById('chart-line').getContext('2d');
    const dataLine = {
        labels: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
        datasets: [{
            label: 'Growth in price index',
            data: [289.53, 272.57, 275.31, 303.42, 328.74, 359.89, 392.57, 424.98, 452.47, 479.25, 514.52, 641.32],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    };
    const configLine = {
        type: 'line',
        data: dataLine,
    };
    const chartLine = new Chart(line, configLine);

    // load pie chart showing area of homes
    const pie = document.getElementById('chart-pie').getContext('2d');
    const dataPie = {
        labels: ['400-600', '700-900', '900-1000', '1000-1200', '1200-1500', '1500-1800', '1800-2000', '2000+'],
        datasets: [{
            label: 'Home area in sq.ft',
            data: [4, 26, 26, 23, 15, 4, 1, 1],
            backgroundColor: [
                'rgba(255, 99, 132)',
                'rgba(255, 159, 64)',
                'rgba(255, 205, 86)',
                'rgba(75, 192, 192)',
                'rgba(54, 162, 235)',
                'rgba(153, 102, 255)',
                'rgba(175, 59, 192)',
                'rgba(201, 203, 207)'
            ],
            hoverOffset: 4
        }]
    };
    const configPie = {
        type: 'doughnut',
        data: dataPie,
    };
    const chartPie = new Chart(pie, configPie);
};

// code for hamburger menu
const hamburgerMenu = () => {
    const icon = document.querySelector('.jkr-header-icon');
    const closeIcon = document.querySelector('.jkr-close-header-icon');
    icon?.addEventListener('click', () => {
        document.querySelector('.jkr-header-menu')?.classList.add('is-open');
        closeIcon?.classList.add('is-open');
    });
    closeIcon?.addEventListener('click', () => {
        document.querySelector('.jkr-header-menu')?.classList.remove('is-open');
        closeIcon?.classList.remove('is-open');
    });
};

// code for login/register dialog box
const loginDialog = () => {
    // add toggle behaviour for login/register forms
    const toggleLogin = () => {
        const headers = document.querySelectorAll('.login-headers h2');
        if (headers.length > 0) {
            headers.forEach(header => {
                header.addEventListener('click', () => {
                    document.querySelector('.login-header')?.classList.toggle('active');
                    document.querySelector('.register-header')?.classList.toggle('active');
                    document.querySelector('.login-form')?.classList.toggle('is-open');
                    document.querySelector('.register-form')?.classList.toggle('is-open');
                });
            });
        }
    };
    // open the login dialog box
    const loginIcon = document.querySelector('.jkr-header-account img');
    const closeLoginIcon = document.querySelector('.jkr-close-login-icon');
    loginIcon?.addEventListener('click', () => {
        document.querySelector('.login-modal')?.classList.add('is-open');
    });
    closeLoginIcon?.addEventListener('click', () => {
        document.querySelector('.login-modal')?.classList.remove('is-open');
    });
    toggleLogin();
};

// redirect to services page from home
const redirectServices = () => {
    const buttons = document.querySelectorAll('.jkr-content2-card button');
    if(buttons.length > 0) {
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                window.location.href = 'services.html';
            });
        })
    }
};

// initialize the carousel on homepage
const initCarousel = () => {
    if (document.querySelector('.jkr-content3')) {
        let index = 0;
        startCarousel();

        function startCarousel() {
            let i;
            let images = document.getElementsByClassName("jkr-listing");
            for (i = 0; i < images.length; i++) {
                images[i].style.display = "none";
            }
            index++;
            if (index > images.length) {index = 1}
            images[index-1].style.display = "block";
            setTimeout(startCarousel, 2000);
        }
    }
};

const logoutUser = () => {
    const logoutBtn = document.querySelector('.jkr-header-user');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            sessionStorage.removeItem('first_name');
            window.location.href = 'index.html';
        });
    }
};

const loginUser = () => {
    const userLoggedIn = document.querySelector('.jkr-header-user');
    if (userLoggedIn) {
        sessionStorage.setItem('first_name', userLoggedIn.innerText);
    }
    if (sessionStorage.getItem('first_name')) {
        const loginDiv = document.querySelector('.jkr-header-account');
        if (loginDiv) {
            loginDiv.innerHTML = "<div class='jkr-header-user'>" + sessionStorage.getItem('first_name') + "</div>"
            logoutUser();
        }
    }
};