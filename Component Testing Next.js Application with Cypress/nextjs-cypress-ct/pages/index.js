import Head from 'next/head'
import Image from 'next/image'
import Posts from '../component/posts'
import styles from '../styles/Home.module.css'

const apiUrl = 'https://jsonplaceholder.typicode.com'

export async function getStaticProps() {
  const postsResponse = await fetch(`${apiUrl}/posts`)
  const posts = await postsResponse.json()
  const usersResponse = await fetch(`${apiUrl}/users`)
  const users = await usersResponse.json()
  return {
    props: {
      posts: posts.slice(0, 10),
      users,
    }
  }
}

export default function Home(props) {
  const { posts, users } = props
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Posts posts={posts} users={users} />

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}