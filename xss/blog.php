<!--
-- Esempi utilizzati nell'elaborato per l'esame di maturità 2020
--	   Copyright (C) 2020  Michele Viotto
-->
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Blog - Viotto Michele</title>
  </head>
  <body>
    <form action="blog.php" method="get">
      Nome: <input type="text" name="author" value=""> <br>
      Testo: <input type="text" name="post_body" value=""> <br>
      <input type="submit">
    </form>

    <?php
      ini_set('display_errors', '1');
      ini_set('display_startup_errors', '1');
      error_reporting(E_ALL);
      $conn = new mysqli("localhost", "user", "password", "tesina");

      # aggiungo un nuovo post
      if(isset($_GET["author"]) && isset($_GET["post_body"])) {
        $author = htmlspecialchars($_GET["author"]);
        $body = htmlspecialchars($_GET["post_body"]);
        $sql = "INSERT INTO posts (author, body) VALUES ('$author', '$body')";
        $conn->query($sql);
        echo "<meta http-equiv=\"refresh\" content=\"0;URL=blog.php\">";
      }

      # mostra tutti i post
      $posts = $conn->query("SELECT author, body FROM posts");
      if ($posts->num_rows > 0) {
        foreach ($posts as $post) {
          echo "<b>" . htmlspecialchars($post['author']) . "</b>: " . htmlspecialchars($post['body']) . "<br>";
        }
      }

      $conn->close();
    ?>
  </body>
</html>
