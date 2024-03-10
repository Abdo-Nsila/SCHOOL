const form = document.querySelector('form');
const results = document.querySelector('#results');
const addImage = (label, src, res) => {
		let sec = document.createElement('section');
		sec.innerHTML = `
		<h2>${label}</h2>
		<div>
			<a href="${src}"><img src="${src}" alt="${label}"></a>
			<small>${res}</small>
		</div>
		`;
		return sec;
	}

const getthumbs = e => {
	e.preventDefault();
	results.innerHTML = '';
	let url = document.querySelector('#webp').checked ? 'vi_webp' : 'vi';
	let extension = document.querySelector('#webp').checked ? 'webp' : 'jpg';
	const video_id = document.querySelector('#video_id').value;
	if(video_id === '') {
		results.innerHTML = '<p>Please enter a valid video ID</p>';
	} else {
	let images = [
		{
			l: 'Player Background',
			r: '(480x360)',
			i: `https://i.ytimg.com/${url}/${video_id}/0.${extension}`
		},{
			l: 'Start frame',
			r: '(120x90)',
			i: `https://i.ytimg.com/${url}/${video_id}/1.${extension}`
		},{
			l: 'Middle frame',
			r: '(120x90)',
			i: `https://i.ytimg.com/${url}/${video_id}/2.${extension}`
		},{
			l: 'End frame',
			r: '(120x90)',
			i: `https://i.ytimg.com/${url}/${video_id}/3.${extension}`
		},{
			l: 'Lowest quality',
			r: '(120x90)',
			i: `https://i.ytimg.com/${url}/${video_id}/default.${extension}`
		},{
			l: 'Medium quality',
			r: '(320x180)',
			i: `https://i.ytimg.com/${url}/${video_id}/mqdefault.${extension}`
		},{
			l: 'High quality',
			r: '(480x360)',
			i: `https://i.ytimg.com/${url}/${video_id}/hqdefault.${extension}`
		},{
			l: 'Standard quality',
			r: '(640x480)',
			i: `https://i.ytimg.com/${url}/${video_id}/sddefault.${extension}`
		},{
			l: 'Unscaled resolution',
			r: '(1280x720)',
			i: `https://i.ytimg.com/${url}/${video_id}/maxresdefault.${extension}`
		}
	];
	images.forEach((image) => {
		results.appendChild(addImage(image.l, image.i, image.r));
	});
	}
}   
document.querySelector('#dummyid').addEventListener('click', (e) => {
	e.preventDefault();
	document.querySelector('#video_id').value = 'dQw4w9WgXcQ';
	getthumbs(e);
});
form.addEventListener('submit', getthumbs);
