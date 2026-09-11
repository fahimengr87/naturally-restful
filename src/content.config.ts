import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Articles live as markdown files in src/content/articles/.
 * Drop a new .md file in → it appears on the site. That's the whole workflow.
 *
 * type:
 *   - 'article'    → informational content; may carry ad slots
 *   - 'review'     → single-product focus; NO ads (affiliate page)
 *   - 'comparison' → multi-product; NO ads (affiliate page)
 */
const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    type: z.enum(['article', 'review', 'comparison']).default('article'),
    products: z
      .array(
        z.object({
          name: z.string(),
          slug: z.string(),      // must exist in public/_redirects as /go/<slug>
          blurb: z.string(),
          badge: z.string().optional(),
        })
      )
      .optional(),
  }),
});

export const collections = { articles };
