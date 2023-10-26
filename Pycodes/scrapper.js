const axios = require('axios');
const cheerio = require('cheerio');
const puppeteer = require('puppeteer');
const fs = require('fs');

const url = 'https://ecampus.dscu.ac.kr/local/ubdoc/?id=23385&tp=m&pg=ubfile';
const downloadFolder = '/Users/leejungbin/Desktop/codes/windowprogramming/';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(url);

  const iframeSrc = await page.evaluate(() => {
    const iframe = document.querySelector('iframe');
    return iframe ? iframe.src : null;
  });

  if (iframeSrc) {
    // Use Axios to fetch iframe content asynchronously
    try {
      const iframeResponse = await axios.get(iframeSrc);
      const iframeHtml = iframeResponse.data;

      // Load iframe content into Cheerio for DOM manipulation
      const $iframe = cheerio.load(iframeHtml);

      // Your scraping logic here
      // For example, find and download images
      const imgElements = $iframe('img');
      imgElements.each(async (index, element) => {
        const imgSrc = $iframe(element).attr('src');
        if (imgSrc) {
          try {
            const imgResponse = await axios.get(imgSrc, { responseType: 'arraybuffer' });
            const imgData = Buffer.from(imgResponse.data, 'binary');
            const imgFileName = `image${index}.png`;
            const imgPath = `${downloadFolder}/${imgFileName}`;
            fs.writeFileSync(imgPath, imgData);
            console.log(`Downloaded: ${imgPath}`);
          } catch (error) {
            console.error(`Error downloading image: ${imgSrc}`);
          }
        }
      });
    } catch (error) {
      console.error('Error fetching iframe content:', error);
    }
  } else {
    console.log('No iframe found on the page.');
  }

  await browser.close();
})();


