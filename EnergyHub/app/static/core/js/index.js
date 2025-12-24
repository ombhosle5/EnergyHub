// const mountainLeft = document.querySelector('#mountain_left');
// const mountainRight = document.querySelector('#mountain_right');
// const cloud1 = document.querySelector('#clouds_1');
// const cloud2 = document.querySelector('#clouds_2');
// const text = document.querySelector('#text');
// const man = document.querySelector('#man');

// /* Respect reduced motion preference */
// const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// if (!prefersReducedMotion) {
//   let latestScroll = 0;
//   let ticking = false;

//   function onScroll() {
//     latestScroll = window.scrollY;

//     if (!ticking) {
//       window.requestAnimationFrame(updateParallax);
//       ticking = true;
//     }
//   }

//   function updateParallax() {
//     const value = latestScroll;

//     mountainLeft.style.transform = `translateX(-${value / 0.7}px)`;
//     mountainRight.style.transform = `translateX(${value / 0.7}px)`;

//     cloud1.style.transform = `translateX(${value * 2}px)`;
//     cloud2.style.transform = `translateX(-${value * 2}px)`;

//     text.style.transform = `translateY(-${value}px)`;

//     const scale = Math.max(0.6, 1 - value / window.innerHeight);
//     man.style.transform = `scale(${scale})`;

//     ticking = false;
//   }

//   window.addEventListener('scroll', onScroll, { passive: true });
// }


const mountainLeft = document.querySelector('#mountain_left');
const mountainRight = document.querySelector('#mountain_right');
const cloud1 = document.querySelector('#clouds_1');
const cloud2 = document.querySelector('#clouds_2');
const text = document.querySelector('#text');
const man = document.querySelector('#man');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    mountainLeft.style.left = `-${value/0.7}px`
    cloud2.style.left = `-${value*2}px`
    mountainRight.style.left = `${value/0.7}px`
    cloud1.style.left = `${value*2}px`
    text.style.bottom = `-${value}px`;
    man.style.height = `${window.innerHeight - value}px`
})