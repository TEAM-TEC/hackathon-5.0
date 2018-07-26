<html>
<h1>Fetching Potholes Details,Please Wait for a while</h1>
<?php
exec("python plotpothole.py");
header("Location: m1.html");
?>
</html>