// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded');
    
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    console.log('signUpButton:', signUpButton);
    console.log('signInButton:', signInButton);
    console.log('container:', container);

    if (signUpButton && signInButton && container) {
        console.log('All elements found! Setting up event listeners...');
        
        signUpButton.addEventListener('click', () => {
            console.log('Sign Up button clicked');
            container.classList.add("right-panel-active");
            console.log('Added class - container classes:', container.className);
        });

        signInButton.addEventListener('click', () => {
            console.log('Sign In button clicked');
            container.classList.remove("right-panel-active");
            console.log('Removed class - container classes:', container.className);
        });
    } else {
        console.log('Elements not found!');
        console.log('signUpButton found:', !!signUpButton);
        console.log('signInButton found:', !!signInButton);
        console.log('container found:', !!container);
    }
});

