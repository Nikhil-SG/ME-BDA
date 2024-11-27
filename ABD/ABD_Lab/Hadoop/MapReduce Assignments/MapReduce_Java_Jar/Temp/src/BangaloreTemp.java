import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class BangaloreTemp {

    // Mapper class
    public static class BangaloreTempMapper extends Mapper<LongWritable, Text, Text, FloatWritable> {
        private static final String CITY_FILTER = "Bangalore";  // The city to filter

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String[] token = line.split("\\s+");  // Handles multiple spaces or tabs

            // Ensure token array has the required length
            if (token.length >= 3) {
                String city = token[2];  // Get city name from the third token

                // Filter for the city 'Bangalore'
                if (city.equals(CITY_FILTER)) {
                    try {
                        float temperature = Float.parseFloat(token[1]); 
                        context.write(new Text(city), new FloatWritable(temperature)); // Emit city and temperature
                    } catch (NumberFormatException e) {
                        e.printStackTrace();  // Log parsing errors
                    }
                }
            }
        }
    }

    // Reducer class
    public static class BangaloreTempReducer extends Reducer<Text, FloatWritable, Text, Text> {
        public void reduce(Text key, Iterable<FloatWritable> values, Context context) throws IOException, InterruptedException {
            float max = -Float.MAX_VALUE; // Use proper extreme values for max and min
            float min = Float.MAX_VALUE;

            // Iterate over values to find max and min temperatures for Bangalore
            for (FloatWritable val : values) {
                float temp = val.get();
                if (temp < min) {
                    min = temp;
                }
                if (temp > max) {
                    max = temp;
                }
            }
            // Output the max and min temperatures as a formatted string
            String result = String.join(", ", "Max Temp: " + max, "Min Temp: " + min);
            context.write(key, new Text(result));
        }
    }

    // Main method
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "bangalore temperature analysis");

        job.setJarByClass(BangaloreTemp.class);
        job.setMapperClass(BangaloreTempMapper.class);
        job.setReducerClass(BangaloreTempReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
