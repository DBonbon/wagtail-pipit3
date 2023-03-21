/* global module */

import React from 'react';
import BlogPage from './BlogPage';
import data from './BlogPage.data';

const BlogPageStory = {
    title: 'Containers/BlogPage',
    component: BlogPage,
};
export default BlogPageStory;

export const BlogPageWithData = () => <BlogPage {...data} />;
export const BlogPageWithoutData = () => <BlogPage />;
