// 1. Scene, Camera, and Renderer Setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 2. Add Orbit Controls
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// 3. Add Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1.5);
directionalLight.position.set(20, 10, 20);
scene.add(directionalLight);

const planets = [
    {
        name: "La Luna",
        title: "¿Dónde deseas ir?",
        url: "../../renpy_proyecto/luna-1.0-dists/luna-1.0-web/index.html",
        position: new THREE.Vector3(0, 0, 0),
        camDistance: 5,
        minZoom: 2,
        maxZoom: 15,
        model: null
    },
    {
        name: "Marte",
        title: "¿Dónde deseas ir?",
        url: "../../renpy_proyecto/marte-1.0-dists/marte-1.0-web/index.html",
        position: new THREE.Vector3(40, 0, 0),
        camDistance: 8,
        minZoom: 3.5,
        maxZoom: 25,
        model: null
    }
];

let currentIndex = 0;
const targetCamPos = new THREE.Vector3();
const targetLookAt = new THREE.Vector3();
let isTransitioning = false;

// Initial camera setup at index 0 (The Moon)
camera.position.set(0, 0, planets[0].camDistance);
controls.target.copy(planets[0].position);
controls.minDistance = planets[0].minZoom;
controls.maxDistance = planets[0].maxZoom;

const loader = new THREE.GLTFLoader();

// 5. Load the Moon (`moon.glb`)
loader.load('moon.glb', function (gltf) {
    planets[0].model = gltf.scene;
    planets[0].model.position.copy(planets[0].position);
    scene.add(planets[0].model);
}, undefined, (err) => console.error('Moon load error:', err));

// 6. Define Mars using a Clean Sphere, BaseColor, and Normal Map
const textureLoader = new THREE.TextureLoader();

const marsBaseColor = textureLoader.load('material_baseColor.jpeg'); 
const marsNormalMap = textureLoader.load('material_normal.png');   

const marsGeometry = new THREE.SphereGeometry(2, 64, 64);

const marsMaterial = new THREE.MeshStandardMaterial({ 
    map: marsBaseColor,       
    normalMap: marsNormalMap,    
    roughness: 0.8 
});

planets[1].model = new THREE.Mesh(marsGeometry, marsMaterial);
planets[1].model.position.copy(planets[1].position);
scene.add(planets[1].model);

// 7. Navigation Logic & UI Elements
const prevArrow = document.getElementById('prevArrow');
const nextArrow = document.getElementById('nextArrow');
const planetLabel = document.getElementById('planetLabel');
const planetTitle = document.getElementById('planetTitle');
const travelBtn = document.getElementById('travelBtn');

// Textos iniciales
planetLabel.innerText = planets[0].name;
planetTitle.innerText = planets[0].title;

function goToPlanet(index) {
    if (index < 0 || index >= planets.length) return;
    currentIndex = index;
    const planet = planets[currentIndex];

    // Update targets for smooth sliding transition
    targetLookAt.copy(planet.position);
    targetCamPos.set(planet.position.x, planet.position.y, planet.position.z + planet.camDistance);
    
    // Update zoom boundaries for the selected planet's size
    controls.minDistance = planet.minZoom;
    controls.maxDistance = planet.maxZoom;
    isTransitioning = true;

    // Update UI label, title and arrow visibility
    planetLabel.innerText = planet.name;
    planetTitle.innerText = planet.title;
    prevArrow.classList.toggle('hidden', currentIndex === 0);
    nextArrow.classList.toggle('hidden', currentIndex === planets.length - 1);
}

prevArrow.addEventListener('click', () => goToPlanet(currentIndex - 1));
nextArrow.addEventListener('click', () => goToPlanet(currentIndex + 1));

// Evento para el botón Viajar
travelBtn.addEventListener('click', () => {
    const currentPlanet = planets[currentIndex];
    window.location.href = currentPlanet.url;
});

// Support Left/Right keyboard arrow keys
window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') goToPlanet(currentIndex + 1);
    if (e.key === 'ArrowLeft') goToPlanet(currentIndex - 1);
});

// 8. Animation Loop
function animate() {
    requestAnimationFrame(animate);

    // Slow axial rotation
    if (planets[0].model) planets[0].model.rotation.y += 0.001;
    if (planets[1].model) planets[1].model.rotation.y += 0.0012;

    // Smooth space slide
    if (isTransitioning) {
        camera.position.lerp(targetCamPos, 0.04);
        controls.target.lerp(targetLookAt, 0.04);

        if (camera.position.distanceTo(targetCamPos) < 0.05) {
            isTransitioning = false;
        }
    }

    controls.update();
    renderer.render(scene, camera);
}
animate();

// Handle Window Resizing
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});