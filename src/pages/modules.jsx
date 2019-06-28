import React from "react";
import Helmet from "react-helmet";
import { graphql } from "gatsby";
import Layout from "../layout";
import ModuleListing from "../components/ModuleListing/ModuleListing";
import SEO from "../components/SEO/SEO";
import config from "../../data/SiteConfig";

class Module extends React.Component {
  render() {
    const postEdges = this.props.data.allMarkdownRemark.edges;
    return (
      <Layout>
        <div className="index-container">
          <Helmet title={config.siteTitle} />
          <SEO />
          <ModuleListing postEdges={postEdges} />
        </div>
      </Layout>
    );
  }
}

export default Module;

/* eslint no-undef: "off" */
export const moduleQuery = graphql`
  query moduleQuery {
    allMarkdownRemark(
      limit: 2000
      sort: { fields: [fields___date], order: DESC }
      filter: {frontmatter: {posttype: {eq: "module"}}}
    ) {
      edges {
        node {
          fields {
            slug
            date
          }
          excerpt
          timeToRead
          frontmatter {
            title
            tags
            cover
            date
          }
        }
      }
    }
  }
`;
