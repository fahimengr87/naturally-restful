import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const articles = await getCollection('articles');
  const sorted = articles.sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );
  return rss({
    title: 'Naturally Restful',
    description:
      'Honest, research-cited guides to sleep & stress supplements. What works, what doesn\u2019t, and who shouldn\u2019t take it.',
    site: context.site,
    items: sorted.map((a) => ({
      title: a.data.title,
      description: a.data.description,
      pubDate: a.data.pubDate,
      link: `/articles/${a.id}/`,
    })),
    customData: '<language>en-us</language>',
  });
}
