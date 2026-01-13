INSERT INTO geo_buckets (name, centroid_lat, centroid_lng, spatial_index, created_at)
VALUES
  ('sangotedo', 6.4698, 3.6285, ST_GeomFromText('POINT(3.6285 6.4698)', 4326), NOW()),
  ('sangotedo ajah', 6.4720, 3.6301, ST_GeomFromText('POINT(3.6301 6.4720)', 4326), NOW()),
  ('sangotedo lagos', 6.4705, 3.6290, ST_GeomFromText('POINT(3.6290 6.4705)', 4326), NOW());

INSERT INTO properties (title, location_name, lat, lng, price, bedrooms, bathrooms, geo_bucket_id, spatial_index, created_at)
VALUES
  ('Property 1', 'Sangotedo', 6.4698, 3.6285, 100000, 3, 2, 1, ST_GeomFromText('POINT(3.6285 6.4698)', 4326), NOW()),
  ('Property 2', 'Sangotedo, Ajah', 6.4720, 3.6301, 120000, 4, 3, 2, ST_GeomFromText('POINT(3.6301 6.4720)', 4326), NOW()),
  ('Property 3', 'sangotedo lagos', 6.4705, 3.6290, 110000, 2, 2, 3, ST_GeomFromText('POINT(3.6290 6.4705)', 4326), NOW());